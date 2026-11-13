# Google-Play-Eintrag — Faithful parents

Das Gegenstück zu `listing.md` (App Store). Die Feldnamen stehen so, wie die Play Console
sie auf Deutsch zeigt; Zeichengrenzen in eckigen Klammern. Wo ein Text schon im
App-Store-Eintrag steht, steht er hier trotzdem vollständig — Play hat andere Grenzen
(z. B. Kurzbeschreibung 80 statt Werbetext 170), und so lässt sich jedes Feld direkt
kopieren.

Die App ist dieselbe wie auf dem iPhone: **zehn Sprachen** — Englisch (*Like a Father* /
*As a Mother Comforts*), Deutsch (*Wie ein Vater* / *Wie eine Mutter tröstet*), Spanisch,
Französisch, Portugiesisch, Türkisch, Russisch, Koreanisch, Vietnamesisch, Indonesisch. Sie folgt der
Sprache des Geräts und lässt sich unter *About/Über* umstellen. Standardsprache des
Eintrags: **Englisch (Vereinigtes Königreich) – en-GB**; Deutsch und die sechs weiteren Sprachen kommen als
Übersetzungen dazu (Teil 4).

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
auf die deutsche, rechtlich verbindliche Fassung (`privacy-de.html`) und auf die Übersetzungen
(`privacy-es/fr/pt/tr/ru/ko.html`, erzeugt mit `tools/app/make_privacy.py`), und alle nennen
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
    • English, German, Spanish, French, Portuguese, Turkish, Russian and Korean — the app follows your phone's language, and you can switch it.

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
    • Acht Sprachen (Deutsch, Englisch, Spanisch, Französisch, Portugiesisch, Türkisch, Russisch, Koreanisch) – die App folgt der Sprache deines Geräts und lässt sich umstellen.

    Beide Bücher stützen sich auf veröffentlichte Bibelwissenschaft; die Anmerkungen nennen die Werke hinter jedem Tag. Die Bibelzitate der deutschen Ausgabe sind eigene Übersetzungen aus dem Hebräischen und Griechischen.

Die sechs folgenden Sprachen haben eine aufgenommene Lesung (Näheres in `listing.md`, Teil 3b). Alle Texte sind maschinell
übersetzt — vor dem Einreichen von Muttersprachlern prüfen lassen. Grafiken und Screenshots:
leer lassen (Play zeigt dann die englischen).

## Spanisch (Spanien) – es-ES

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Dos devocionales de 31 días sobre los padres y las madres de la Biblia.

### Vollständige Beschreibung [4000]

    Dos devocionales de treinta y un días en una sola app: Como un padre, sobre los padres de la Biblia, y Como una madre consuela, sobre sus madres. Lee uno, lee el otro, o léelos juntos.

    Los padres de la Biblia no son una galería de héroes. Abraham levanta el cuchillo sobre su hijo. Elí no frena a los suyos. David llora demasiado tarde. Sara empuja a una esclava al desierto; Rebeca engaña a su marido; Raquel y Lea libran su rivalidad con los nombres de sus hijos. Junto a ellos están Ana, que oró; Rizpa, que guardó a sus hijos muertos durante meses; Jocabed, que construyó un pequeño arca; Job, que oró por hijos a los que no podía controlar; Manoa, que preguntó cómo; y el padre de Lucas 15, que corrió.

    Cada día trae:

    • una lectura breve de la Biblia y un versículo clave
    • una palabra del hebreo o del griego, con lo que significa
    • una página en lenguaje claro sobre un padre o una madre
    • dos preguntas para pensar
    • una oración y algo que hacer hoy
    • notas y fuentes, si quieres comprobar el terreno que pisa cada día

    SIETE PLANES DE LECTURA

    • Lado a lado — los dos libros juntos, 31 días
    • Como un padre — 31 días
    • Como una madre consuela — 31 días
    • Enseñar a tus hijos — 8 días
    • Cuando los padres se equivocan — 8 días
    • Duelo y pérdida — 7 días
    • Si un padre o una madre te hizo daño — 7 días

    Un plan nunca se te escapa. Si dejas pasar una semana, te espera donde lo dejaste.

    SINCERO CON LOS PASAJES DUROS

    Estos libros no esquivan los textos difíciles: las frases sobre la vara en Proverbios, las hijas, los padres que hicieron daño y los lectores a quienes sus propios padres hirieron. Donde los estudiosos discrepan, las notas lo dicen.

    PENSADA PARA LEER

    • Funciona del todo sin conexión. Sin inicio de sesión, sin cuenta, sin publicidad.
    • Tu progreso de lectura se queda en tu dispositivo.
    • Claro y oscuro, y texto que puedes agrandar.
    • Puede leerte cada día en voz alta, con una voz grabada o con la voz de tu dispositivo; las lecturas se pueden descargar para escuchar sin conexión.

    Ambos devocionales se apoyan en estudios bíblicos publicados, y las notas nombran las obras que hay detrás de cada día. Las citas bíblicas de la edición española son traducciones propias del autor a partir del hebreo y del griego.

    También en inglés, alemán, francés, portugués, turco, ruso y coreano. La app sigue el idioma de tu dispositivo.

## Französisch (Frankreich) – fr-FR

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Deux livres de méditation de 31 jours sur les pères et mères de la Bible.

### Vollständige Beschreibung [4000]

    Deux livres de méditation de trente et un jours dans une seule app : Comme un père, sur les pères de la Bible, et Comme une mère console, sur ses mères. Lis l’un, lis l’autre, ou lis-les côte à côte.

    Les parents de la Bible ne forment pas une galerie de héros. Abraham lève le couteau sur son fils. Éli ne retient pas les siens. David pleure trop tard. Sara pousse une servante dans le désert ; Rébecca trompe son mari ; Rachel et Léa mènent leur rivalité à travers les noms de leurs enfants. À leurs côtés se tiennent Anne, qui a prié ; Ritspa, qui a veillé ses fils morts pendant des mois ; Yokèbèd, qui a fabriqué une petite arche ; Job, qui a prié pour des enfants qu’il ne maîtrisait pas ; Manoach, qui a demandé comment faire ; et le père de Luc 15, qui a couru.

    Chaque jour apporte :

    • une courte lecture biblique et un verset clé
    • un mot de l’hébreu ou du grec, avec son sens
    • une page en langage clair sur un père ou une mère
    • deux questions pour réfléchir
    • une prière et une chose à faire aujourd’hui
    • des notes et des sources, si tu veux vérifier le terrain sous un jour

    SEPT PLANS DE LECTURE

    • Côte à côte — les deux livres ensemble, 31 jours
    • Comme un père — 31 jours
    • Comme une mère console — 31 jours
    • Enseigner tes enfants — 8 jours
    • Quand les parents se trompent — 8 jours
    • Deuil et perte — 7 jours
    • Si un parent t’a fait du mal — 7 jours

    Un plan ne te file jamais entre les doigts. Si tu laisses passer une semaine, il t’attend là où tu t’es arrêté.

    HONNÊTE SUR LES PASSAGES DIFFICILES

    Ces livres n’évitent pas les textes que l’on trouve difficiles : les sentences sur la verge dans les Proverbes, les filles, les pères qui ont fait du mal, et les lecteurs que leurs propres parents ont blessés. Là où les spécialistes ne sont pas d’accord, les notes le disent.

    CONÇUE POUR LIRE

    • Fonctionne entièrement hors connexion. Aucune connexion, aucun compte, aucune publicité.
    • Ta progression reste sur ton appareil.
    • Clair et sombre, et un texte que tu peux agrandir.
    • Peut te lire chaque jour à voix haute, avec une voix enregistrée ou celle de ton appareil ; les lectures se téléchargent pour écouter hors connexion.

    Les deux livres s’appuient sur des études bibliques publiées, et les notes nomment les ouvrages derrière chaque jour. Les citations bibliques de l’édition française sont des traductions personnelles de l’auteur à partir de l’hébreu et du grec.

    Aussi en anglais, allemand, espagnol, portugais, turc, russe et coréen. L’app suit la langue de ton appareil.

## Portugiesisch (Brasilien) – pt-BR

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Dois devocionais de 31 dias sobre os pais e as mães da Bíblia.

### Vollständige Beschreibung [4000]

    Dois devocionais de trinta e um dias em um só app: Como um pai, sobre os pais da Bíblia, e Como uma mãe consola, sobre as mães. Leia um, leia o outro, ou leia os dois lado a lado.

    Os pais da Bíblia não são uma galeria de heróis. Abraão levanta a faca sobre o filho. Eli não contém os seus. Davi chora tarde demais. Sara empurra uma escrava para o deserto; Rebeca engana o marido; Raquel e Léia travam a rivalidade pelos nomes dos filhos. Ao lado deles estão Ana, que orou; Rispa, que guardou por meses os filhos mortos; Joquebede, que fez uma pequena arca; Jó, que orou por filhos que não podia controlar; Manoá, que perguntou como; e o pai de Lucas 15, que correu.

    Cada dia traz:

    • uma leitura bíblica curta e um versículo-chave
    • uma palavra do hebraico ou do grego, com o seu sentido
    • uma página em linguagem simples sobre um pai ou uma mãe
    • duas perguntas para pensar
    • uma oração e uma coisa para fazer hoje
    • notas e fontes, se você quiser conferir o chão debaixo de um dia

    SETE PLANOS DE LEITURA

    • Lado a lado — os dois livros juntos, 31 dias
    • Como um pai — 31 dias
    • Como uma mãe consola — 31 dias
    • Ensinar seus filhos — 8 dias
    • Quando os pais erram — 8 dias
    • Luto e perda — 7 dias
    • Se um pai ou uma mãe feriu você — 7 dias

    Um plano nunca foge de você. Se passar uma semana, ele espera onde você parou.

    HONESTO COM AS PARTES DIFÍCEIS

    Estes livros não pulam os textos que as pessoas acham difíceis: os ditos sobre a vara em Provérbios, as filhas, os pais que causaram dano e os leitores que foram feridos pelos próprios pais. Onde os estudiosos divergem, as notas dizem.

    FEITO PARA LER

    • Funciona totalmente offline. Sem login, sem conta, sem publicidade.
    • Seu progresso de leitura fica no seu aparelho.
    • Claro e escuro, e texto que você pode aumentar.
    • Pode ler cada dia em voz alta, com uma voz gravada ou a voz do seu aparelho; as leituras podem ser baixadas para ouvir offline.

    Os dois devocionais se apoiam em estudos bíblicos publicados, e as notas citam as obras por trás de cada dia. As citações bíblicas da edição em português são traduções próprias do autor a partir do hebraico e do grego.

    Também em inglês, alemão, espanhol, francês, turco, russo e coreano. O app segue o idioma do seu aparelho.

## Türkisch – tr-TR

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Kutsal Kitap’ın babaları ve anneleri üzerine 31 günlük iki kitap.

### Vollständige Beschreibung [4000]

    Tek uygulamada otuz bir günlük iki kitap: Kutsal Kitap’ın babalarını anlatan Bir Baba Gibi ve annelerini anlatan Bir Anne Avuttuğu Gibi. Birini oku, ötekini oku ya da ikisini yan yana oku.

    Kutsal Kitap’ın ebeveynleri bir kahramanlar galerisi değildir. İbrahim oğlunun üzerine bıçağı kaldırır. Eli oğullarını engellemez. Davut çok geç ağlar. Sara bir cariyeyi çöle sürer; Rebeka kocasını aldatır; Rahel ile Lea çocuklarının adları üzerinden çekişir. Yanlarında dua eden Hanna; ölü oğullarını aylarca bekleyen Rispa; küçük bir sepet yapan Yokebed; denetleyemediği çocukları için dua eden Eyüp; “nasıl” diye soran Manoah; ve Luka 15’teki, koşan baba durur.

    Her gün şunları getirir:

    • kısa bir Kutsal Kitap okuması ve bir anahtar ayet
    • İbranice ya da Yunancadan bir sözcük ve anlamı
    • bir baba ya da bir anne üzerine sade bir sayfa
    • düşünmek için iki soru
    • bir dua ve bugün yapılacak bir şey
    • bir günün dayandığı zemini denetlemek istersen notlar ve kaynaklar

    YEDİ OKUMA PLANI

    • Yan yana — iki kitap birlikte, 31 gün
    • Bir Baba Gibi — 31 gün
    • Bir Anne Avuttuğu Gibi — 31 gün
    • Çocuklarına öğretmek — 8 gün
    • Anne babalar hata yaptığında — 8 gün
    • Yas ve kayıp — 7 gün
    • Bir ebeveyn seni incittiyse — 7 gün

    Bir plan senden hiç kaçmaz. Bir hafta kaçırırsan, kaldığın yerde bekler.

    ZOR YERLERDE DÜRÜST

    Bu kitaplar insanların zor bulduğu metinleri atlamaz: Süleyman’ın Meselleri’ndeki değnek sözleri, kızlar, zarar veren babalar ve kendi ebeveynleri tarafından incitilmiş okurlar. Bilginlerin ayrıştığı yerde notlar bunu söyler.

    OKUMAK İÇİN YAPILDI

    • Tamamen çevrimdışı çalışır. Giriş yok, hesap yok, reklam yok.
    • Okuma ilerlemen cihazında kalır.
    • Açık ve koyu tema, büyütebileceğin metin.
    • Her günü kayıtlı bir sesle ya da cihazının sesiyle sesli okuyabilir; okumalar çevrimdışı dinlemek için indirilebilir.

    İki kitap da yayımlanmış Kutsal Kitap araştırmalarına dayanır; notlar her günün arkasındaki eserleri adıyla anar. Türkçe baskıdaki Kutsal Kitap alıntıları, yazarın İbranice ve Yunancadan kendi çevirileridir.

    İngilizce, Almanca, İspanyolca, Fransızca, Portekizce, Rusça ve Korece de var. Uygulama cihazının dilini izler.

## Russisch – ru-RU

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Две книги на 31 день об отцах и матерях Библии, с планами чтения.

### Vollständige Beschreibung [4000]

    Две книги на тридцать один день в одном приложении: «Как отец» — об отцах Библии и «Как утешает мать» — о её матерях. Читайте одну, читайте другую или обе рядом.

    Родители Библии — не галерея героев. Авраам поднимает нож над сыном. Илий не останавливает своих сыновей. Давид плачет слишком поздно. Сарра изгоняет рабыню в пустыню; Ревекка обманывает мужа; Рахиль и Лия ведут своё соперничество через имена детей. Рядом с ними — Анна, которая молилась; Рицпа, которая месяцами охраняла погибших сыновей; Иохевед, которая сделала маленький ковчег; Иов, который молился о детях, над которыми был не властен; Маной, который спросил, как; и отец из Евангелия от Луки, глава 15, который побежал навстречу.

    В каждом дне:

    • короткий библейский отрывок и ключевой стих
    • слово из древнееврейского или греческого и его значение
    • страница простым языком об одном отце или одной матери
    • два вопроса для размышления
    • молитва и одно дело на сегодня
    • примечания и источники — если хотите проверить почву под ногами в этом дне

    СЕМЬ ПЛАНОВ ЧТЕНИЯ

    • Рядом — обе книги вместе, 31 день
    • Как отец — 31 день
    • Как утешает мать — 31 день
    • Учить своих детей — 8 дней
    • Когда родители ошибаются — 8 дней
    • Горе и утрата — 7 дней
    • Если родитель причинил тебе боль — 7 дней

    План никогда не убегает от вас. Пропустите неделю — он ждёт там, где вы остановились.

    ЧЕСТНО О ТРУДНОМ

    Эти книги не обходят места, которые считают трудными: изречения о розге в Притчах, дочерей, отцов, причинивших вред, и читателей, которых ранили собственные родители. Где учёные расходятся, примечания говорят об этом.

    СОЗДАНО ДЛЯ ЧТЕНИЯ

    • Работает полностью без сети. Без входа, без аккаунта, без рекламы.
    • Твой прогресс чтения остаётся на вашем устройстве.
    • Светлая и тёмная темы, текст можно увеличить.
    • Каждый день можно прослушать в записи или голосом вашего устройства; записи можно скачать для прослушивания без сети.

    Обе книги опираются на опубликованные библейские исследования, а примечания называют труды, стоящие за каждым днём. Библейские цитаты русского издания — собственные переводы автора с древнееврейского и греческого.

    Есть также на английском, немецком, испанском, французском, португальском, турецком и корейском. Приложение следует языку вашего устройства.

## Koreanisch – ko-KR

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    성경 속 아버지와 어머니를 다룬 31일 묵상집 두 권, 읽기 계획 포함.

### Vollständige Beschreibung [4000]

    서른하루씩의 묵상집 두 권을 한 앱에 담았습니다. 성경 속 아버지들을 다룬 「아버지처럼」과 어머니들을 다룬 「어머니가 위로하듯」입니다. 한 권씩 읽어도 좋고, 나란히 읽어도 좋습니다.

    성경 속 부모는 영웅들의 전시관이 아닙니다. 아브라함은 아들 위로 칼을 듭니다. 엘리는 자기 아들들을 막지 못합니다. 다윗은 너무 늦게 웁니다. 사라는 여종을 광야로 내몰고, 리브가는 남편을 속이며, 라헬과 레아는 자녀의 이름으로 다툼을 이어 갑니다. 그 곁에는 기도한 한나, 죽은 아들들을 몇 달 동안 지킨 리스바, 작은 상자를 만든 요게벳, 마음대로 할 수 없는 자녀들을 위해 기도한 욥, “어떻게 해야 합니까” 하고 물은 마노아, 그리고 달려간 누가복음 15장의 아버지가 서 있습니다.

    날마다 이런 내용이 있습니다.

    • 짧은 성경 본문과 핵심 구절
    • 히브리어나 헬라어 단어 하나와 그 뜻
    • 한 아버지나 한 어머니에 관한 쉬운 글 한 쪽
    • 생각해 볼 질문 두 가지
    • 기도와 오늘 해 볼 한 가지
    • 그날의 바탕을 확인하고 싶을 때 볼 수 있는 주석과 출처

    일곱 가지 읽기 계획

    • 나란히 — 두 권을 함께, 31일
    • 아버지처럼 — 31일
    • 어머니가 위로하듯 — 31일
    • 자녀를 가르치기 — 8일
    • 부모가 잘못할 때 — 8일
    • 슬픔과 상실 — 7일
    • 부모에게 상처받았다면 — 7일

    계획은 결코 당신을 앞서 달아나지 않습니다. 한 주를 건너뛰어도 멈춘 자리에서 기다립니다.

    어려운 대목도 정직하게

    이 책들은 사람들이 어렵게 여기는 본문을 건너뛰지 않습니다. 잠언의 매 이야기, 딸들, 해를 끼친 아버지들, 그리고 자기 부모에게 상처받은 독자들을 다룹니다. 학자들의 견해가 갈리는 곳은 주석이 그렇게 밝힙니다.

    읽기 위해 만들었습니다

    • 인터넷 없이도 완전히 작동합니다. 로그인도 계정도 광고도 없습니다.
    • 읽기 진행 상황은 기기에 남습니다.
    • 밝은 화면과 어두운 화면, 키울 수 있는 글자.
    • 날마다의 글을 녹음된 음성이나 기기의 음성으로 들을 수 있고, 내려받아 오프라인으로도 들을 수 있습니다.

    두 책 모두 출판된 성경 연구에 기대고 있으며, 주석은 날마다의 근거 저작을 밝힙니다. 한국어판의 성경 인용은 저자가 히브리어와 헬라어에서 직접 옮긴 번역입니다.

    영어, 독일어, 스페인어, 프랑스어, 포르투갈어, 터키어, 러시아어로도 볼 수 있습니다. 앱은 기기의 언어를 따릅니다.

## Vietnamesisch – vi

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Suy niệm 31 ngày về cha mẹ trong Kinh Thánh, có kế hoạch đọc và bản đọc thu âm.

### Vollständige Beschreibung [4000]

    Hai cuốn sách suy niệm ba mươi mốt ngày trong một ứng dụng: Như một người cha, về những người cha trong Kinh Thánh, và Như người mẹ ủi an, về những người mẹ. Đọc cuốn này, đọc cuốn kia, hoặc đọc song hành cả hai.

    Những người cha trong Kinh Thánh không phải là một dãy anh hùng. Áp-ra-ham giơ dao lên con mình. Ê-li không kiềm chế được các con. Đa-vít khóc quá muộn. Sa-ra đẩy một nữ tỳ ra sa mạc; Rê-bê-ca lừa chồng; Ra-chên và Lê-a tranh đua nhau qua tên các con. Bên cạnh họ là An-ne, người đã cầu nguyện; Rít-pa, người suốt nhiều tháng canh giữ các con đã chết; Giô-kê-bết, người đã làm một chiếc giỏ nhỏ; Gióp, người cầu nguyện cho những đứa con ông không thể kiểm soát; Ma-nô-a, người đã hỏi phải làm thế nào; và người cha trong Lu-ca 15, người đã chạy ra đón con.

    Mỗi ngày gồm có:

    • một bài đọc Kinh Thánh ngắn và một câu then chốt
    • một từ tiếng Hê-bơ-rơ hoặc Hy Lạp, cùng ý nghĩa của nó
    • một trang viết bằng lời giản dị về một người cha hoặc một người mẹ
    • hai câu hỏi để suy ngẫm
    • một lời cầu nguyện và một việc để làm hôm nay
    • ghi chú và nguồn tham khảo, nếu bạn muốn xem nền móng của một ngày

    BẢY KẾ HOẠCH ĐỌC

    • Song hành — hai cuốn sách cùng nhau, 31 ngày
    • Như một người cha — 31 ngày
    • Như người mẹ ủi an — 31 ngày
    • Dạy dỗ con cái — 8 ngày
    • Khi cha mẹ lầm lỗi — 8 ngày
    • Đau buồn và mất mát — 7 ngày
    • Nếu cha hoặc mẹ đã làm bạn tổn thương — 7 ngày

    Kế hoạch không bao giờ bỏ rơi bạn. Nếu một tuần trôi qua, nó vẫn chờ ở chỗ bạn dừng lại.

    THẲNG THẮN VỚI NHỮNG PHẦN KHÓ

    Hai cuốn sách này không bỏ qua những đoạn mà người ta thấy khó: những câu nói về cây roi trong Châm Ngôn, các cô con gái, những người cha đã gây tổn hại, và những độc giả đã bị chính cha mẹ mình làm tổn thương. Ở chỗ các học giả bất đồng, phần ghi chú sẽ nói rõ.

    LÀM RA ĐỂ ĐỌC

    • Hoạt động hoàn toàn khi không có mạng. Không đăng nhập, không tài khoản, không quảng cáo.
    • Tiến trình đọc của bạn nằm trên thiết bị của bạn.
    • Nền sáng và tối, và chữ có thể phóng to.
    • Có thể đọc thành tiếng từng ngày, bằng giọng thu âm sẵn hoặc giọng của thiết bị; các bản đọc có thể tải xuống để nghe khi không có mạng.

    Hai cuốn sách suy niệm này dựa trên các nghiên cứu Kinh Thánh đã được công bố, và phần ghi chú nêu các công trình đứng sau từng ngày. Các đoạn trích Kinh Thánh trong bản tiếng Việt là bản dịch riêng của tác giả từ tiếng Hê-bơ-rơ và tiếng Hy Lạp.

    Cũng có bằng tiếng Anh, tiếng Đức, tiếng Tây Ban Nha, tiếng Pháp, tiếng Bồ Đào Nha, tiếng Thổ Nhĩ Kỳ, tiếng Nga và tiếng Hàn. Ứng dụng theo ngôn ngữ của thiết bị bạn.

## Indonesisch – id

### App-Name [30]

    Faithful parents

### Kurzbeschreibung [80]

    Dua buku renungan 31 hari tentang para bapa dan ibu dalam Alkitab.

### Vollständige Beschreibung [4000]

    Dua buku renungan tiga puluh satu hari dalam satu aplikasi: Seperti Seorang Bapa, tentang para bapa dalam Alkitab, dan Seperti Ibu yang Menghibur, tentang para ibu. Bacalah yang satu, bacalah yang lain, atau bacalah keduanya berdampingan.

    Para orang tua dalam Alkitab bukanlah deretan pahlawan. Abraham mengangkat pisau atas anaknya. Eli tidak menahan anak-anaknya. Daud menangis terlambat. Sara mengusir seorang hamba perempuan ke padang gurun; Ribka menipu suaminya; Rahel dan Lea berseteru lewat nama anak-anak mereka. Di samping mereka ada Hana, yang berdoa; Rizpa, yang berbulan-bulan menjaga anak-anaknya yang telah mati; Yokhebed, yang membuat sebuah keranjang kecil; Ayub, yang mendoakan anak-anak yang tidak dapat ia kendalikan; Manoah, yang bertanya bagaimana; dan sang bapa dalam Lukas 15, yang berlari.

    Setiap hari menghadirkan:

    • satu bacaan Alkitab yang singkat dan satu ayat kunci
    • satu kata dari bahasa Ibrani atau Yunani, beserta artinya
    • satu halaman berbahasa sederhana tentang seorang bapa atau seorang ibu
    • dua pertanyaan untuk direnungkan
    • satu doa dan satu hal untuk dilakukan hari ini
    • catatan dan sumber, jika Anda ingin memeriksa dasar dari sebuah hari

    TUJUH RENCANA BACA

    • Berdampingan — kedua buku bersama, 31 hari
    • Seperti Seorang Bapa — 31 hari
    • Seperti Ibu yang Menghibur — 31 hari
    • Mengajar anak-anak Anda — 8 hari
    • Ketika orang tua keliru — 8 hari
    • Duka dan kehilangan — 7 hari
    • Jika ayah atau ibu pernah melukai Anda — 7 hari

    Sebuah rencana tidak pernah meninggalkan Anda. Jika seminggu terlewat, rencana itu menunggu di tempat Anda berhenti.

    JUJUR TERHADAP BAGIAN YANG SULIT

    Buku-buku ini tidak melewati teks-teks yang dianggap sulit: perkataan tentang tongkat dalam Amsal, para putri, orang tua yang menyebabkan luka, dan pembaca yang dilukai oleh orang tuanya sendiri. Di mana para ahli berbeda pendapat, catatan-catatan mengatakannya.

    DIRANCANG UNTUK DIBACA

    • Berfungsi sepenuhnya tanpa koneksi. Tanpa login, tanpa akun, tanpa iklan.
    • Kemajuan membaca Anda tersimpan di perangkat Anda.
    • Mode terang dan gelap, dan teks yang dapat diperbesar.
    • Setiap hari dapat dibacakan dengan suara perangkat Anda.

    Kedua buku renungan ini bertumpu pada kajian Alkitab yang telah diterbitkan, dan catatan-catatannya menyebut karya-karya di balik setiap hari. Kutipan Alkitab dalam edisi bahasa Indonesia adalah terjemahan sendiri penulis dari bahasa Ibrani dan Yunani.

    Tersedia juga dalam bahasa Inggris, Jerman, Spanyol, Prancis, Portugis, Turki, Rusia, dan Korea. Aplikasi mengikuti bahasa perangkat Anda.

## So kommt eine Sprache dazu (Deutsch und die sechs weiteren)

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
- Play bietet an, fehlende Sprachen **automatisch** zu übersetzen. Für die acht
  Sprachen der App nicht nötig; für weitere Sprachen besser nicht einschalten — sonst
  verspricht der Eintrag eine Sprache, die die App nicht hat.
- Die Datenschutz-URL gilt für alle Sprachen gemeinsam (Teil 3).

## Versionshinweise („Was ist neu") [500, je Sprache]

Werden beim Anlegen des Releases eingetragen, nicht im Store-Eintrag. Format im Feld:

    <en-GB>
    First release.
    </en-GB>
    <de-DE>
    Erste Version.
    </de-DE>
    (die übrigen sechs Sprachen: <es-ES> First release → "Primera versión.", <fr-FR>
    "Première version.", <pt-BR> "Primeira versão.", <tr-TR> "İlk sürüm.", <ru-RU>
    "Первая версия.", <ko-KR> "첫 번째 버전.")

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
