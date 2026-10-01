# Google-Play-Eintrag — Faithful parents

Das Gegenstück zu `listing.md` (App Store). Die Feldnamen stehen so, wie die Play Console
sie auf Deutsch zeigt; Zeichengrenzen in eckigen Klammern. Wo ein Text schon im
App-Store-Eintrag steht, steht er hier trotzdem vollständig — Play hat andere Grenzen
(z. B. Kurzbeschreibung 80 statt Werbetext 170), und so lässt sich jedes Feld direkt
kopieren.

Die App ist dieselbe wie auf dem iPhone: **Englisch und Deutsch**, *Like a Father* /
*As a Mother Comforts* und *Wie ein Vater* / *Wie eine Mutter tröstet*. Sie folgt der
Sprache des Geräts und lässt sich unter *About/Über* umstellen. Standardsprache des
Eintrags: **Englisch (Vereinigtes Königreich) – en-GB**; Deutsch kommt als Übersetzung
dazu (Teil 4).

Reihenfolge der Arbeit:

1. Entwicklerkonto anlegen (Teil 1) — dauert wegen der Identitätsprüfung ein paar Tage.
2. Upload-Schlüssel erzeugen und die App bauen (Teil 2).
3. App in der Play Console anlegen, *App-Inhalte* ausfüllen (Teil 3), Eintrag auf Englisch
   und Deutsch (Teil 4).
4. **Geschlossener Test mit mindestens 12 Testern über 14 Tage** (Teil 6) — erst danach
   lässt Google die App in die Produktion. Das ist der längste Schritt; früh anfangen.

---

# Teil 1 — Registrierung als Entwickler

## Was man braucht

    Google-Konto:        am besten ein eigenes für die Veröffentlichung, nicht das private
                         Gmail-Postfach (es lässt sich später nicht übertragen)
    Gebühr:              25 US-$, einmalig, per Kreditkarte
    Ausweis:             Personalausweis oder Reisepass (Identitätsprüfung)
    Telefonnummer:       wird per SMS bestätigt
    Android-Gerät:       ein eigenes Android-Handy; Google verlangt bei neuen Konten,
                         dass man sich einmal mit der Play-Console-App darauf anmeldet
    Kontakt-E-Mail:      revelation-today@web.de (wird im Store öffentlich gezeigt)

## Privatperson oder Organisation?

**Empfehlung: „Für mich selbst" (privates Konto).** Das passt zum App-Store-Eintrag
(Copyright „2026 Hagen Schilder") und braucht keine D-U-N-S-Nummer. Eine Organisation
lohnt sich erst, wenn ein Verein oder Verlag dahinter steht; ein Wechsel ist später über
eine Kontoübertragung möglich.

Was das private Konto mit sich bringt:

- Der öffentliche Entwicklername ist frei wählbar (z. B. *Hagen Schilder* oder
  *Revelation Today*). Die Postanschrift wird bei kostenlosen Apps ohne In-App-Käufe
  **nicht** öffentlich angezeigt.
- **Pflichttest vor der Veröffentlichung** (Teil 6): 12 Tester, 14 Tage am Stück.

## Schritte

1. <https://play.google.com/console/signup> öffnen, mit dem Veröffentlichungs-Konto anmelden.
2. **„Für mich selbst"** wählen.
3. Entwicklerprofil: öffentlicher Entwicklername, Kontakt-E-Mail
   `revelation-today@web.de`, Telefonnummer, optional Website
   `https://revelation-today.github.io/parents/`.
4. Fragen zur Erfahrung mit Android-Apps ehrlich beantworten (hat keine Folgen für die
   Zulassung; Google fragt nur).
5. 25 US-$ bezahlen.
6. **Identität bestätigen:** Name und Anschrift müssen genau so eingetragen sein wie auf
   dem Ausweis (und wie im Zahlungsprofil). Ausweis hochladen. Die Prüfung dauert meist
   1–3 Tage; bis dahin lassen sich Apps anlegen, aber nicht veröffentlichen.
7. **Gerät bestätigen:** Die App *Google Play Console* auf dem Android-Handy
   installieren und sich dort mit demselben Konto anmelden.

---

# Teil 2 — Die App bauen

Gebaut wird ohne Android Studio, genau wie beim iPhone: ein GitHub-Actions-Lauf
(`.github/workflows/android.yml`) erzeugt das Android-Projekt aus `web/`, signiert es und
legt eine `.aab` (für Play) und eine `.apk` (zum Ausprobieren auf dem eigenen Handy) als
Download ab.

## Einmal: den Upload-Schlüssel erzeugen

Play signiert die App selbst („Play App Signing"). Wir signieren nur mit einem
**Upload-Schlüssel**, der beweist, dass eine neue Version von uns kommt. Geht er
verloren, kann man ihn über den Play-Support ersetzen lassen — trotzdem sicher
aufbewahren (Passwort-Manager, nicht in Git, nicht in einem öffentlich geteilten Ordner).

`keytool` gehört zu Java. Einmal installieren (PowerShell):

    winget install EclipseAdoptium.Temurin.21.JDK

Neues Terminal öffnen, dann:

    keytool -genkeypair -v -keystore upload-key.jks -alias upload `
      -keyalg RSA -keysize 2048 -validity 10000 `
      -dname "CN=Hagen Schilder, O=Revelation Today, C=DE"

keytool fragt nach einem Passwort. Moderne keytool-Versionen verwenden es für Datei und
Schlüssel zugleich.

Für GitHub in Text umwandeln:

    [Convert]::ToBase64String([IO.File]::ReadAllBytes("upload-key.jks")) | Set-Clipboard

## Einmal: die Geheimnisse in GitHub eintragen

Repository *revelation-today/parents* → *Settings → Secrets and variables → Actions →
New repository secret*:

    ANDROID_KEYSTORE_B64        (aus der Zwischenablage, s. o.)
    ANDROID_KEYSTORE_PASSWORD   das Passwort
    ANDROID_KEY_ALIAS           upload
    ANDROID_KEY_PASSWORD        dasselbe Passwort

## Jede Version

1. *Actions → Android build for Google Play → Run workflow*, Version eingeben
   (z. B. `1.0.0`). Die Versionsnummer für Play (versionCode) ist die Laufnummer und
   steigt dadurch immer.
2. Nach etwa 5–10 Minuten liegt unten auf der Seite des Laufs unter *Artifacts* eine
   ZIP-Datei mit `faithful-parents-1.0.0-N.aab` und `…apk`.
3. **Zum Ausprobieren** die `.apk` aufs Handy kopieren und öffnen (Android fragt einmal,
   ob Installationen aus dieser Quelle erlaubt sind).
4. **Für Play** die `.aab` in der Play Console hochladen (Teil 6). Ab dem zweiten Upload
   kann das der Workflow selbst (Teil 5).

## Vor dem ersten Hochladen auf einem echten Handy prüfen

Die App ist für das iPhone gebaut und auf Android ungetestet. Mit der `.apk`:

- **Zurück-Taste / Zurück-Wischgeste:** führt von einem Tag zurück zur Liste und schließt
  die App erst auf der Startseite.
- **Oben und unten:** Nichts verschwindet unter der Statusleiste oder der
  Navigationsleiste; auch im Dunkelmodus sind die Symbole der Statusleiste lesbar.
- **Vorlesen:** aufgenommene Stimme (mit Internet) und Gerätestimme (im Flugmodus);
  läuft das Vorlesen bei gesperrtem Bildschirm weiter?
- **Herunterladen der Lesungen** und danach Wiedergabe im Flugmodus.
- **Erinnerung:** einschalten → Android fragt nach der Erlaubnis für Benachrichtigungen;
  kommt sie zur eingestellten Zeit (auf Android 14+ kann sie ein paar Minuten später
  kommen — das ist gewollt, die App verlangt keinen „exakten Wecker")?
- **Link „Read …/… lesen"** öffnet den Browser.

---

# Teil 3 — App anlegen und *App-Inhalte*

## App erstellen

Play Console → **App erstellen**:

    App-Name:              Faithful parents
    Standardsprache:       Englisch (Vereinigtes Königreich) – en-GB
    App oder Spiel:        App
    Kostenlos oder kostenpflichtig: Kostenlos
    Erklärungen:           Programmrichtlinien und US-Exportgesetze bestätigen

„Kostenlos" lässt sich später nicht mehr in „kostenpflichtig" ändern.

Der Paketname wird nicht hier eingetragen; er kommt mit der ersten `.aab`:
`net.revelationtoday.parent` (derselbe wie die Bundle-ID beim iPhone). **Er ist danach
für immer an diese App gebunden.**

## Einstellungen → Store-Einstellungen

    App-Kategorie:   Bücher & Nachschlagewerke
    Tags:            (bis zu 5) z. B. Religion, Bücher, Bibel, Andachten
                     — Play schlägt passende vor; nur nehmen, was zutrifft
    E-Mail-Adresse:  revelation-today@web.de
    Website:         https://revelation-today.github.io/parents/
    Telefonnummer:   leer lassen

## Richtlinie → App-Inhalte

Jeder Punkt muss einmal beantwortet werden, sonst lässt sich nichts einreichen.

### Datenschutzerklärung

    https://revelation-today.github.io/parents/privacy.html

Play kennt nur eine URL pro App (nicht pro Sprache). Die englische Seite verweist oben
auf die deutsche, rechtlich verbindliche Fassung (`privacy-de.html`), und beide nennen
jetzt die Android-App bei der Erinnerung. Vor dem Einreichen einmal über *Deploy web app
to Pages* neu veröffentlichen, damit die geänderte Fassung online ist.

### App-Zugriff

    Alle Funktionen sind ohne besonderen Zugriff verfügbar.

(Kein Login, also keine Anmeldedaten für die Prüfer.)

### Anzeigen

    Nein, meine App enthält keine Werbung.

### Einstufung des Inhalts (IARC-Fragebogen)

E-Mail: `revelation-today@web.de`. Kategorie: **Referenz, Nachrichten oder Bildung**
(nicht „Spiel", nicht „Soziales").

Für die Antworten gilt dasselbe wie beim App Store: Die Bücher **erwähnen** Gewalt in
biblischen Erzählungen — die Vergewaltigung Tamars (Tag 24), Hinrichtungen,
Kinderopfer, die „Rute"-Sprüche (Tag 27) — und sprechen Leser an, die als Kind
geschlagen oder verletzt wurden (Tag 30). Nichts davon wird dargestellt oder
ausgemalt. Ehrlich beantworten, d. h. bei Gewalt und bei sexueller Gewalt die Fragen
nach *textlichen Bezügen / Erwähnungen* mit **Ja** beantworten, die nach *Darstellung*,
*Bildern* oder *realistischer/detaillierter Gewalt* mit **Nein**.

    Nutzerinteraktion / Austausch von Inhalten:  Nein
    Teilen des Standorts:                        Nein
    Digitale Käufe:                              Nein
    Glücksspiel / simuliertes Glücksspiel:       Nein
    Drogen, Alkohol, Tabak:                      Nein (nur, falls eine Frage ausdrücklich
                                                 nach biblischem Wein fragt — dann Erwähnung)
    Vulgäre Sprache:                             Nein
    Uneingeschränkter Internetzugang (Browser):  Nein — nur ein Link zum Bibeltext

Das Ergebnis vergibt IARC selbst (USK, PEGI, ESRB usw.). Erwartet wird ungefähr
**USK 12 / PEGI 12**, möglicherweise 16. Wie beim App Store: Falls es höher ausfällt
als erwartet, nicht die Antworten schönen, sondern prüfen, ob irgendwo „Darstellung"
statt „Erwähnung" angekreuzt wurde. Am Inhalt nichts ändern.

### Zielgruppe und Inhalte

    Zielaltersgruppen:            18 und älter (optional zusätzlich 16–17)
    Spricht die App Kinder an?    Nein

**Keine Altersgruppe unter 13 wählen.** Sonst gilt die App als Kinder-App („Families"),
mit zusätzlichen Prüfungen, die zu einem Andachtsbuch für Eltern nicht passen.

### Datensicherheit

    Erfasst oder teilt Ihre App die erforderlichen Arten von Nutzerdaten?   Nein

Damit ist der Fragebogen fast fertig; Play fragt dann nur noch nach der Bestätigung.
Begründung (für einen selbst): Keine Konten, keine Analyse, keine Werbung, kein
Tracking. Lesefortschritt, Pläne, Einstellungen und heruntergeladene Lesungen bleiben
auf dem Gerät. Die Lesungen werden von GitHub Pages geladen — das ist ein Abruf von
Dateien, keine Datenerfassung durch die App. Wenn die Datenschutzerklärung GitHub Pages
als Hoster nennt, passt alles zusammen.

### Behörden-Apps · Finanzfunktionen · Gesundheit · Nachrichten-App

    Behörden-App:        Nein
    Finanzfunktionen:    Meine App bietet keine Finanzfunktionen
    Gesundheit:          Meine App hat keine Gesundheitsfunktionen
    Nachrichten-App:     Nein

### Berechtigungen (falls Play nachfragt)

Die App fordert an: Internet, Benachrichtigungen (für die tägliche Erinnerung,
Android fragt den Nutzer), Neustart erkennen (damit die Erinnerung einen Neustart
übersteht), Wake Lock, `SCHEDULE_EXACT_ALARM`. Keine davon verlangt bei Play eine
eigene Erklärung. Nicht verwendet wird `USE_EXACT_ALARM` — das würde eine Erklärung
verlangen.

### Inhaltsrechte / NIV

Play fragt nicht wie Apple nach Inhalten Dritter. Der Copyright-Hinweis zur NIV steht in
der App unter *About → Translations* und am Ende der englischen Beschreibung (Teil 4).

---

# Teil 4 — Hauptversion des Store-Eintrags, zweisprachig

**Wachstum → Store-Präsenz → Hauptversion des Store-Eintrags.** Zuerst Englisch
ausfüllen (die Standardsprache), dann Deutsch als Übersetzung (unten, „So kommt Deutsch
dazu").

## Grafiken (je Sprache; ohne deutsche zeigt Play die englischen)

    App-Symbol, 512 × 512:          store/play/icon-512.png          (für beide Sprachen)
    Vorstellungsgrafik, 1024 × 500: store/play/feature-en.png
                                    store/play/feature-de.png        (deutsch)
    Smartphone-Screenshots:         store/screenshots/android-phone/        1080 × 2160
                                    store/screenshots/de/android-phone/     (deutsch)
    Tablet-Screenshots 10 Zoll:     store/screenshots/android-tablet/       1600 × 2560
                                    store/screenshots/de/android-tablet/    (deutsch)
    Tablet-Screenshots 7 Zoll:      dieselben wie 10 Zoll

    01-today     Heute, mit zwei laufenden Leseplänen
    02-reading   ein Tag mit hebräischem Wort des Tages
    03-plans     die sieben Lesepläne
    04-library   die Bibliothek (As a Mother Comforts)
    05-dark      ein Tag im Dunkelmodus

Die iPhone-Screenshots gehen bei Play **nicht**: Play lehnt Bilder ab, die länger als
2 : 1 sind. Neu erzeugen mit

    python store/make_screenshots.py --only android-phone android-tablet
    python store/make_screenshots.py --lang de --only android-phone android-tablet
    python store/make_play_graphics.py

Tablet-Screenshots sind freiwillig, aber ohne sie wird die App auf Tablets in Play
schlechter angezeigt.

## Englisch (Vereinigtes Königreich) – en-GB

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Two 31-day devotionals on the fathers and mothers of the Bible, with plans.

### Vollständige Beschreibung [4000]

    Two thirty-one-day devotionals in one app: Like a Father, on the fathers of the Bible, and As a Mother Comforts, on its mothers. Read one, read the other, or read them side by side.

    The Bible's parents are not a gallery of heroes. Abraham raises a knife over his son. Eli will not restrain his. David weeps too late. Sarah drives a slave woman into the desert; Rebekah deceives her husband; Rachel and Leah conduct a rivalry through their children's names. Alongside them stand Hannah, who prayed; Rizpah, who guarded her dead sons for months; Jochebed, who built a small ark; Job, who prayed for children he could not control; Manoah, who asked how; and the father of Luke 15, who ran.

    Each day gives you:

    • a short Bible reading, and a key verse
    • a word from the Hebrew or Greek, with what it means
    • a page of plain writing about one father or one mother
    • two questions to think over
    • a prayer, and one thing to do today
    • notes and sources, if you want to check the ground under a day

    SEVEN READING PLANS

    • Side by Side — both books together, 31 days
    • Like a Father — 31 days
    • As a Mother Comforts — 31 days
    • Teaching Your Children — 8 days
    • When Parents Get It Wrong — 8 days
    • Grief and Loss — 7 days
    • If a Parent Hurt You — 7 days

    A plan never runs away from you. Miss a week, and it waits where you left off.

    TO LISTEN TO

    Every day can be read aloud — by a recorded voice or by your phone's own voice. The text follows along as it is read, and a tap on a paragraph jumps there. The readings can be downloaded for listening offline.

    HONEST ABOUT THE HARD PARTS

    These books do not skip the texts people find difficult: the rod sayings in Proverbs, the daughters, the fathers who did harm, and the readers whose own parents hurt them. Where scholars disagree, the notes say so.

    BUILT FOR READING

    • The texts work completely offline. Nothing to sign in to, no account, no advertising.
    • Your reading progress stays on your device.
    • Light and dark, and text you can make bigger.
    • English and German — the app follows your phone's language, and you can switch it.

    Both devotionals rest on published biblical scholarship, and the notes name the works behind each day.

    Scripture quotations marked NIV are taken from the Holy Bible, New International Version (Anglicised edition). Copyright © 1979, 1984, 2011 by Biblica. Used by permission of Hodder & Stoughton Ltd, an Hachette UK company. All rights reserved. 'NIV' is a registered trademark of Biblica. UK trademark number 1448790.

Play hat kein Feld für Schlüsselbegriffe; gesucht wird im Namen, in der
Kurzbeschreibung und in der Beschreibung. Deshalb stehen dort Wörter wie *devotional*,
*Bible*, *fathers*, *mothers*, *reading plan*. Nicht künstlich wiederholen — Play
wertet Keyword-Stuffing als Richtlinienverstoß.

## Deutsch – de-DE

### App-Name [30]

    Faithful parents

(Wie im App Store: Der Name bleibt englisch, weil er auch auf dem Home-Bildschirm so
heißt. Möglich wäre auch ein deutscher Store-Name wie „Faithful parents – Andachten"
(28 Zeichen); der Name unter dem Symbol auf dem Handy bleibt davon unberührt.)

### Kurzbeschreibung [80]

    Zwei Andachtsbücher über Väter und Mütter der Bibel, je 31 Tage, mit Leseplänen.

### Vollständige Beschreibung [4000]

    Zwei Andachtsbücher mit je 31 Tagen in einer App: „Wie ein Vater" über die Väter der Bibel und „Wie eine Mutter tröstet" über ihre Mütter. Lies das eine, lies das andere, oder lies beide nebeneinander.

    Die Eltern der Bibel sind keine Heldengalerie. Abraham hebt das Messer über seinen Sohn. Eli wehrt seinen Söhnen nicht. David weint zu spät. Sara treibt eine Sklavin in die Wüste; Rebekka täuscht ihren Mann; Rahel und Lea tragen ihren Streit über die Namen ihrer Kinder aus. Daneben stehen Hanna, die ihr Herz vor Gott ausschüttete; Rizpa, die ihre toten Söhne monatelang bewachte; Jochebed, die ihrem Sohn eine kleine Arche baute; Hiob, der für Kinder betete, die er nicht in der Hand hatte; Manoach, der fragte, wie; und der Vater aus Lukas 15, der seinem Sohn entgegenlief.

    Jeder Tag enthält:

    • einen kurzen Bibelabschnitt und einen Schlüsselvers
    • ein Wort aus dem Hebräischen oder Griechischen und was es bedeutet
    • eine Seite über einen Vater oder eine Mutter, in klarer Sprache
    • zwei Fragen zum Nachdenken
    • ein Gebet und eine Sache für heute
    • Anmerkungen und Quellen, wenn du den Boden unter einem Tag prüfen willst

    SIEBEN LESEPLÄNE

    • Seite an Seite – beide Bücher zusammen, 31 Tage
    • Wie ein Vater – 31 Tage
    • Wie eine Mutter tröstet – 31 Tage
    • Deine Kinder lehren – 8 Tage
    • Wenn Eltern Fehler machen – 8 Tage
    • Trauer und Verlust – 7 Tage
    • Wenn Vater oder Mutter dir wehgetan haben – 7 Tage

    Kein Plan läuft dir davon. Verpasst du eine Woche, wartet er dort, wo du aufgehört hast.

    ZUM HÖREN

    Jeder Tag kann vorgelesen werden – von einer aufgenommenen Stimme oder von der Stimme deines Geräts. Der Text läuft beim Vorlesen mit, und ein Tipp auf einen Absatz springt dorthin. Die Lesungen lassen sich für unterwegs aufs Gerät laden.

    EHRLICH BEI DEN SCHWEREN STELLEN

    Diese Bücher lassen die schwierigen Texte nicht aus: die Rute in den Sprüchen, die Töchter, die Väter, die Schaden angerichtet haben, und die Leser, denen die eigenen Eltern wehgetan haben. Wo die Forschung uneins ist, sagen es die Anmerkungen.

    ZUM LESEN GEBAUT

    • Die Texte funktionieren vollständig offline. Keine Anmeldung, kein Konto, keine Werbung.
    • Dein Lesefortschritt bleibt auf deinem Gerät.
    • Hell und dunkel, und Text, den du größer stellen kannst.
    • Deutsch und Englisch – die App folgt der Sprache deines Geräts und lässt sich umstellen.

    Beide Bücher stützen sich auf veröffentlichte Bibelwissenschaft; die Anmerkungen nennen die Werke hinter jedem Tag. Die Bibelzitate der deutschen Ausgabe sind eigene Übersetzungen aus dem Hebräischen und Griechischen.

## So kommt Deutsch dazu

1. *Wachstum → Store-Präsenz → Hauptversion des Store-Eintrags*.
2. Oben **Übersetzungen verwalten → Eigene Übersetzungen hinzufügen** (nicht
   „Übersetzungen kaufen").
3. **Deutsch – de-DE** anhaken → *Übernehmen*.
4. Oben erscheint jetzt eine Sprachauswahl. *Deutsch – de-DE* wählen; die Felder sind
   mit dem englischen Text vorbelegt oder leer — durch die deutschen Texte oben ersetzen.
5. Deutsche Vorstellungsgrafik und deutsche Screenshots hochladen.
6. **Speichern.**

Was dabei zu wissen ist:

- de-DE wird allen gezeigt, deren Play Store auf Deutsch steht — auch in Österreich und
  der Schweiz. Eigene Einträge für de-AT oder de-CH sind nicht nötig.
- Fehlt ein Feld in der deutschen Übersetzung, zeigt Play dort den englischen Text.
- Play bietet an, fehlende Sprachen **automatisch** zu übersetzen. Für Deutsch nicht
  nötig; für andere Sprachen besser nicht einschalten, solange die App selbst nur
  Englisch und Deutsch spricht — sonst verspricht der Eintrag eine Sprache, die die App
  nicht hat.
- Die Datenschutz-URL gilt für alle Sprachen gemeinsam (Teil 3).

## Versionshinweise („Was ist neu") [500, je Sprache]

Werden beim Anlegen des Releases eingetragen, nicht im Store-Eintrag. Format im Feld:

    <en-GB>
    First release.
    </en-GB>
    <de-DE>
    Erste Version.
    </de-DE>

---

# Teil 5 — Hochladen aus GitHub (freiwillig, ab der zweiten Version)

Die **erste** `.aab` muss von Hand in der Play Console hochgeladen werden (Teil 6); erst
danach nimmt Play Uploads über die Schnittstelle an. Danach spart das Folgende das
Herunterladen und Hochladen:

1. <https://console.cloud.google.com> → neues Projekt (z. B. *faithful-parents-play*) →
   *APIs & Dienste* → **Google Play Android Developer API** aktivieren.
2. *IAM & Verwaltung → Dienstkonten* → Dienstkonto erstellen (keine Rollen nötig) →
   *Schlüssel → Schlüssel hinzufügen → JSON*. Die Datei wird heruntergeladen.
3. Play Console → **Nutzer und Berechtigungen → Neue Nutzer einladen** → die E-Mail
   des Dienstkontos (`…@…iam.gserviceaccount.com`) → App-Berechtigung für
   *Faithful parents*: **Releases verwalten** (Test- und Produktions-Tracks).
4. In GitHub ein weiteres Secret: `PLAY_SERVICE_ACCOUNT_JSON` = der ganze Inhalt der
   JSON-Datei. Die Datei danach löschen.

Beim Workflow dann *track* und *status* wählen. Solange die App noch nie veröffentlicht
war, nimmt Play nur **status = draft** an; den Entwurf gibt man dann in der Play Console
frei.

---

# Teil 6 — Test und Veröffentlichung

## Interner Test (sofort, bis zu 100 Tester, keine Prüfung)

1. *Testen und veröffentlichen → Testen → Interner Test → Neuen Release erstellen*.
2. Beim ersten Mal: **Play App-Signatur** bestätigen (von Google verwaltet —
   empfohlen, Standard).
3. `.aab` hochladen, Versionshinweise (Teil 4), *Speichern → Überprüfen → Einführung*.
4. *Tester* → E-Mail-Liste anlegen (die eigene Adresse reicht zunächst) → den
   **Link zur Teilnahme** auf dem Handy öffnen → App aus Play installieren.

So lässt sich die App schon aus Play testen, bevor irgendetwas geprüft ist.

## Geschlossener Test — Pflicht für private Konten

Neue private Entwicklerkonten dürfen erst in die Produktion, wenn ein **geschlossener
Test** lief: **mindestens 12 Tester, die 14 Tage ohne Unterbrechung dabei sind.**

1. *Testen → Geschlossener Test* → einen Track anlegen (z. B. *Freunde*).
2. Länder: alle, oder mindestens Deutschland, Österreich, Schweiz, Vereinigtes Königreich.
3. Tester per E-Mail-Liste (Google-Konten = die Adressen, mit denen sie im Play Store
   angemeldet sind) oder per Google-Gruppe.
4. Release mit derselben `.aab` erstellen und **zur Prüfung senden** — der geschlossene
   Test wird schon von Google geprüft (meist 1–3 Tage).
5. Den Teilnahme-Link an die Tester schicken. Jeder muss **über den Link beitreten und
   die App installieren**; zählt erst dann.
6. Nach 14 Tagen: *Dashboard → Zugriff auf Produktion beantragen*. Google fragt dort,
   wie getestet wurde, was die Tester zurückgemeldet haben und was geändert wurde. Mit
   ein, zwei konkreten Sätzen beantworten (z. B. „Tester fanden X, in Version 1.0.1
   behoben").

Praktisch: 15 bis 20 Leute einladen (Familie, Gemeinde, Hauskreis), damit auch dann 12
dabei bleiben, wenn jemand austritt oder die App löscht. Die Tester sollten sie
wirklich öffnen und benutzen; Google sieht, ob das geschieht. Ein neues Release während
des Tests ist erlaubt und macht den Antrag glaubwürdiger.

## Produktion

1. *Testen und veröffentlichen → Produktion → Länder/Regionen*: alle (wie im App Store).
2. *Neuen Release erstellen* → die getestete `.aab` aus der Bibliothek übernehmen →
   Versionshinweise → **Zur Prüfung senden**.
3. Die erste Prüfung dauert bei neuen Konten oft einige Tage bis eine Woche.

## Was sonst noch zu wissen ist

- **Zielplattform:** Play verlangt jedes Jahr (Stichtag 31. August) ein aktuelles
  `targetSdkVersion`. Capacitor 8 erfüllt die Vorgabe für 2026; im Jahr darauf reicht
  meist ein Update von `@capacitor/android` und ein neuer Lauf des Workflows.
- **Inaktive Konten:** Google schließt Entwicklerkonten, die lange nichts veröffentlicht
  und sich nicht angemeldet haben. Einmal im Jahr eine Version oder wenigstens ein
  Login genügt.
- **Die Web-App** bleibt daneben bestehen; auf Android bietet Chrome sie ohnehin zum
  Installieren an. Wer die Play-Version hat, braucht sie nicht.
