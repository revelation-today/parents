/*
  Service worker: offline reading for the web version.

  The whole app is one page plus fonts and icons, so everything is stored on
  first visit. The page itself is network first, so a reader who is online
  always gets the current text; everything else is cache first.
  VERSION is rewritten by tools/app/build_app.py on every build, which clears
  the old copies.

  If this ever misbehaves, deploy a sw.js whose whole body is
  `self.registration.unregister()`.
*/
const VERSION = '1a6f9f3eb98e';
const CACHE = 'parents-' + VERSION;
const FILES = [
  './', 'index.html', 'manifest.webmanifest', 'fonts/fonts.css',
  'icons/apple-touch-icon.png', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/favicon-64.png'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('parents-') && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put('index.html', copy)); return res; })
        .catch(() => caches.match('index.html'))
    );
    return;
  }
  event.respondWith(
    caches.match(req).then(hit => hit || fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    }))
  );
});
