"""App Store screenshots, rendered from the real app.

    python store/make_screenshots.py

Renders web/index.html in an iframe of exactly the phone's logical size, at
three times the pixel density, and crops the result to Apple's required
dimensions: 6.9" (1320x2868) and 6.5" (1242x2688).
The app is seeded with a plan in progress so the screens look lived-in.
"""
import json, pathlib, shutil, subprocess, tempfile, time
from datetime import date, timedelta
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
APP = ROOT / "web/index.html"
OUT = ROOT / "store/screenshots"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SIZES = {"6.9": (440, 956), "6.5": (414, 896)}
SCALE = 3

now = int(time.time() * 1000)
read = {f"{b}{n}": {"r": True, "t": now} for b in "FM" for n in range(1, 8)}
STATE = {"read": read,
         "plans": {"side": {"start": (date.today() - timedelta(days=7)).isoformat(), "t": now, "stopped": False},
                   "teach": {"start": (date.today() - timedelta(days=2)).isoformat(), "t": now, "stopped": False}},
         "font": 1, "last": "F4", "t": now}

SEED = """<script>
const __M = {'like-a-father-as-a-mother-v1': %s};
try { Object.defineProperty(window, 'localStorage', {configurable: true, value: {
  getItem: k => (k in __M ? __M[k] : null), setItem: (k, v) => { __M[k] = String(v); },
  removeItem: k => { delete __M[k]; }, clear: () => {} }}); } catch (e) {}
%s
</script>
""" % (json.dumps(json.dumps(STATE)), "")

SHOTS = [
    ("01-today", "#/today", False),
    ("02-reading", "#/read/F4", False),
    ("03-plans", "#/plans", False),
    ("04-library", "#/library/M", False),
    ("05-dark", "#/read/M1", True),
]


def main():
    work = pathlib.Path(tempfile.mkdtemp(prefix="shots-"))
    shutil.copytree(ROOT / "web", work / "web", dirs_exist_ok=True)
    page = (work / "web/index.html").read_text(encoding="utf-8")
    for dark in (False, True):
        seed = SEED
        if dark:
            seed = seed.replace("</script>", "document.documentElement.dataset.theme = 'dark';\n</script>")
        name = "seeded-dark.html" if dark else "seeded.html"
        (work / "web" / name).write_text(page.replace("<body>", "<body>\n" + seed, 1), encoding="utf-8")

    for label, (w, h) in SIZES.items():
        dest = OUT / label
        dest.mkdir(parents=True, exist_ok=True)
        for name, route, dark in SHOTS:
            src = ("seeded-dark.html" if dark else "seeded.html") + route
            frame = work / f"frame-{label}-{name}.html"
            frame.write_text(
                f'<body style="margin:0;background:{"#101514" if dark else "#F4F6F2"}">'
                f'<iframe src="web/{src}" style="width:{w}px;height:{h}px;border:0;display:block"></iframe>',
                encoding="utf-8")
            raw = work / f"raw-{label}-{name}.png"
            subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-first-run",
                            f"--user-data-dir={work / 'edge'}", "--hide-scrollbars",
                            f"--force-device-scale-factor={SCALE}",
                            f"--window-size={max(w + 120, 560)},{h + 40}",
                            "--virtual-time-budget=8000", f"--screenshot={raw}",
                            frame.as_uri()], check=True)
            # Edge returns before the file is on disk.
            for _ in range(120):
                if raw.exists() and raw.stat().st_size > 0:
                    time.sleep(0.4)
                    break
                time.sleep(0.5)
            else:
                raise SystemExit(f"no screenshot written: {raw}")
            img = Image.open(raw).convert("RGB").crop((0, 0, w * SCALE, h * SCALE))
            assert img.size == (w * SCALE, h * SCALE), img.size
            img.save(dest / f"{name}.png")
            print("OK", dest / f"{name}.png", img.size)
    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
