# Like a Father, As a Mother

Two thirty-one-day devotionals on the fathers and mothers of the Bible — *Like a Father* and *As a Mother Comforts* — as an iPhone app and an installable web app, with seven reading plans.

| Where | What |
|---|---|
| `web/` | The finished app: one page (`index.html`), fonts, icons, the web-app manifest and an offline service worker. The iPhone app carries exactly these files. |
| `resources/` | The app icon and splash screens the iOS build is made from. |
| `.github/workflows/pages.yml` | Publishes `web/` to GitHub Pages on every push that changes it. |
| `.github/workflows/ios.yml` | Builds the iPhone app on a Mac runner and uploads it to TestFlight. Run by hand. |
| `capacitor.config.json` | App ID `net.revelationtoday.parents`, home-screen name "Parents". |

## Where the text comes from

`web/index.html` is generated — never edit it by hand. The books live in the book project
(`Dropbox/Bibel/fathers`, `output/devotional/*.md`). After changing them:

```
python tools/app/build_app.py      # in the book project; rewrites web/index.html and web/sw.js here
git add web && git commit -m "…" && git push
```

The push republishes the web version. For the iPhone app, run the iOS workflow again (next section).

## The iPhone app

It is built without a Mac: a GitHub Actions macOS runner creates the Xcode project with
[Capacitor](https://capacitorjs.com), signs it with an App Store Connect API key (Xcode cloud signing),
and uploads it.

**Once, in App Store Connect**

1. *Users and Access → Integrations → App Store Connect API*: create a key with the **Admin** role.
   Download the `.p8` file (possible only once) and note the Key ID and the Issuer ID.
2. *Apps → + → New App*: platform iOS, name **Like a Father, As a Mother**, bundle ID
   `net.revelationtoday.parents` (if it is not offered yet, register it under
   *Certificates, Identifiers & Profiles → Identifiers* first), SKU e.g. `parents-1`.
3. In this repository, *Settings → Secrets and variables → Actions*, add:
   `APPLE_TEAM_ID`, `APPSTORE_KEY_ID`, `APPSTORE_ISSUER_ID`, and `APPSTORE_KEY_P8`
   (the whole text of the `.p8` file).

**Each release**

1. *Actions → iOS build to TestFlight → Run workflow*, enter the version (e.g. `1.0.0`).
   The build number is the workflow's run number, so it always goes up.
2. About 10–20 minutes after the run finishes, the build appears under *TestFlight* in App Store Connect.
   Install it on your iPhone with the TestFlight app.
3. To publish: add the build to a version in App Store Connect, fill in the listing, and submit for review.

**For the App Store listing**

- Privacy policy URL: `https://revelation-today.github.io/parents/privacy.html` (or the custom domain, once set).
- Support and privacy contact: revelation-today@web.de
- App Privacy: *Data Not Collected* — progress is stored only on the device.
- Category: Books (or Reference).
- Scripture quotations marked NIV: the notice required by Biblica is in the app under *About → Translations*.

## The web version

GitHub Pages must be switched on once (*Settings → Pages → Source: GitHub Actions*), and the deploy workflow is started by hand: *Actions → Deploy web app to Pages → Run workflow*.
On iPhone, Safari shows a small hint to add the app to the home screen; after that it opens full-screen and works offline.
