# App Store-Eintrag — Faithful parents

Die Feldnamen stehen so, wie App Store Connect sie auf Deutsch zeigt.
Zeichengrenzen in eckigen Klammern.

Die App gibt es **auf Englisch und Deutsch**: *Like a Father* / *As a Mother Comforts*
und *Wie ein Vater* / *Wie eine Mutter tröstet*. Sie folgt der Sprache des Geräts und lässt
sich unter *About/Über* umstellen. Die Primärsprache des Eintrags bleibt Englisch (UK);
der deutsche Eintrag (Teil 3) beschreibt die deutsche Ausgabe.

---

# Teil 1 — Felder ohne Sprache

## Allgemeine Informationen — *eingetragen*

    Bundle-ID:     net.revelationtoday.parent
    SKU:           faithful-parents
    Apple-ID:      6813810391
    Primärsprache: Englisch (UK)
    Kategorie:     Bücher · Lifestyle

## Inhaltsrechte → „Informationen zu den Inhaltsrechten einrichten"

Die App enthält Inhalte Dritter: in der englischen Ausgabe Bibelzitate aus der New
International Version (Anglicised). Die deutsche Ausgabe zitiert nur eigene Übersetzungen
des Autors und enthält keine Inhalte Dritter. Antwort:

    Ja — die App enthält, zeigt oder greift auf Inhalte Dritter zu,
    und ich habe die Rechte, diese Inhalte zu verwenden.

Begründung (falls nachgefragt): Die Zitate liegen innerhalb der Standardgenehmigung
von Biblica (weniger als 500 Verse, unter 25 % des Werks); der vorgeschriebene
Copyright-Hinweis steht in der App unter *About → Translations* und unten in der
Beschreibung.

## Copyright

    2026 Hagen Schilder

## Altersfreigaben → „Altersfreigaben einrichten"

**Ergebnis: 16+** (Stand 1.0). Die Bücher *erwähnen* Gewalt in biblischen
Erzählungen — die Vergewaltigung Tamars (Tag 24), Hinrichtungen, Kinderopfer,
und die „Rute"-Sprüche der Sprüche Salomos (Tag 27) — und sie sprechen Leser an,
die als Kind geschlagen oder verletzt wurden (Tag 30). Nichts davon wird
dargestellt oder ausgemalt; es wird benannt und seelsorglich eingeordnet.
16+ ist damit eine ehrliche Einstufung, und sie sollte bei künftigen Versionen
gleich beantwortet werden.

Für die Zielgruppe — Eltern — ist die Einstufung praktisch ohne Nachteil: sie
verhindert weder Verkauf noch Prüfung, sondern erscheint nur als Badge und in
Familienfiltern.

Antworten, die gleich bleiben:

    In-App-Steuerelemente:   Uneingeschränkter Internetzugriff = Nein
                             (nur ein optionaler Link zum Bibeltext: BibleGateway.com
                             auf Englisch, bibleserver.com auf Deutsch)
    Benutzergenerierte Inhalte / Soziale Medien: Nein
    Sexualität/Nacktheit:    Keine (keine Darstellung; Tag 24 nennt eine
                             Vergewaltigung, ohne sie zu schildern)
    Medizin oder Wellness:   Keine
    Zufallsbasierte Akt.:    Keine
    Glücksspiel:             Nein

Falls die Einstufung einmal niedriger ausfallen soll, ist der ehrliche Weg nicht,
die Antworten zu ändern, sondern zu prüfen, ob bei Gewalt versehentlich
„häufig/intensiv" statt „selten/mild" gewählt wurde. Am Inhalt sollte nichts
geändert werden: die harten Kapitel sind der Grund, warum die Bücher
vertrauenswürdig sind.

## Dokumentation zur App-Verschlüsselung

Nichts hochzuladen. Der Build setzt bereits `ITSAppUsesNonExemptEncryption = false`
in der Info.plist (die App nutzt nur die Verschlüsselung des Betriebssystems, z. B.
HTTPS beim optionalen Link).

## App-Datenschutz (Vertrauen und Sicherheit → App-Datenschutz)

    Datenschutzrichtlinie-URL: https://revelation-today.github.io/parents/privacy.html
    Datenerfassung:            „Es werden keine Daten von dieser App erfasst."

    Keine Accounts, keine Analyse, keine Werbung, kein Tracking.
    Lesefortschritt und Einstellungen bleiben auf dem Gerät.

## Hinweise für die App-Prüfung (App-Prüfungsinformationen → Anmerkungen)

„Anmeldung erforderlich" bleibt **aus** — die App hat keinen Login.

    This is a self-contained reading app, not a wrapper around a website.

    • All text — two complete 31-day devotionals, 62 readings, in English and German — is
      bundled in the app. It works with the device in airplane mode; please feel free to test it
      that way. The app follows the device language; About → Language switches it.
    • Read aloud: recorded narration is streamed from the app's own website
      (revelation-today.github.io/parents) and can be downloaded for offline listening; without
      a connection the app reads with the device's built-in voice.
    • The app has no accounts and no server. Reading plans, progress, marked days and
      text size are stored on the device.
    • The only outbound link is optional: on each day, "Read <passage>" opens that Bible
      passage in the browser (BibleGateway.com in English, bibleserver.com in German), for
      readers who want the full chapter.
    • To see the plans in action: Plans → Side by Side → Start, then Today.

    No sign-in is required, so no demo account is needed.

## Preisgestaltung und Verfügbarkeit

    Preis:          Kostenlos
    Verfügbarkeit:  alle Länder und Regionen (oder nach Wunsch einschränken)

## App-Vorschauen und Screenshots

    iPhone 6,9 Zoll (1320 × 2868):  store/screenshots/6.9/
    iPhone 6,5 Zoll (1242 × 2688):  store/screenshots/6.5/
    iPad 13 Zoll  (2064 × 2752):    store/screenshots/ipad-13/

    Die App läuft auch auf dem iPad (Capacitor baut universal), deshalb verlangt
    App Store Connect auch iPad-Screenshots.

    01-today     Today, mit zwei laufenden Leseplänen
    02-reading   ein Tag mit hebräischem Wort des Tages
    03-plans     die sieben Lesepläne
    04-library   die Bibliothek (As a Mother Comforts)
    05-dark      ein Tag im Dunkelmodus

    Die Screenshots zeigen die englische App. Für den deutschen Eintrag sind deutsche
    Screenshots besser; make_screenshots.py kann sie erzeugen, wenn es die Sprache „de"
    setzt (noch nicht eingebaut). Lässt man sie bei einer Sprache leer, zeigt der Store
    die der Primärsprache.

---

# Teil 2 — Englisch (UK), die Primärsprache

## Name [30]

    Faithful parents

## Untertitel [30]

    Devotional for parents

## Werbetext [170]

    Two thirty-one-day devotionals on the fathers and mothers of the Bible — with reading plans, the Hebrew behind each day, and notes that show their sources.

## Beschreibung [4000]

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

    HONEST ABOUT THE HARD PARTS

    These books do not skip the texts people find difficult: the rod sayings in Proverbs, the daughters, the fathers who did harm, and the readers whose own parents hurt them. Where scholars disagree, the notes say so.

    BUILT FOR READING

    • Works completely offline. Nothing to sign in to, no account, no advertising.
    • Your reading progress stays on your device.
    • Light and dark, and text you can make bigger.

    Both devotionals rest on published biblical scholarship, and the notes name the works behind each day.

    Also in German: Wie ein Vater and Wie eine Mutter tröstet. The app follows your device's language.

    Scripture quotations marked NIV are taken from the Holy Bible, New International Version (Anglicised edition). Copyright © 1979, 1984, 2011 by Biblica. Used by permission of Hodder & Stoughton Ltd, an Hachette UK company. All rights reserved. 'NIV' is a registered trademark of Biblica. UK trademark number 1448790.

## Schlüsselbegriffe [100, mit Komma getrennt, ohne Leerzeichen]

    devotional,bible,fathers,mothers,parents,reading plan,christian,daily,prayer,family,hebrew,faith

## Support-URL

    https://revelation-today.github.io/parents/

## Marketing-URL (optional)

    https://revelation-today.github.io/parents/

## Neue Funktionen in dieser Version

    First release.

---

# Teil 3 — Deutsch

Die App ist auf Deutsch vollständig: beide Bücher, alle 62 Tage, die Lesepläne und die
Vorlesefunktion. Der Name bleibt „Faithful parents", weil er auch auf dem Home-Bildschirm
so heißt; Untertitel und Beschreibung sind deutsch und nennen die deutschen Buchtitel.

## Name [30]

    Faithful parents

## Untertitel [30]

    Andachten für Väter und Mütter

## Werbetext [170]

    Zwei Andachtsbücher über die Väter und Mütter der Bibel, je 31 Tage – mit Leseplänen, dem hebräischen Wort des Tages, Quellen und Vorlesen. Auf Deutsch und Englisch.

## Beschreibung [4000]

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

    Scripture quotations in the English edition marked NIV are taken from the Holy Bible, New International Version (Anglicised edition). Copyright © 1979, 1984, 2011 by Biblica. Used by permission of Hodder & Stoughton Ltd, an Hachette UK company. All rights reserved. 'NIV' is a registered trademark of Biblica. UK trademark number 1448790.

## Schlüsselbegriffe [100, mit Komma getrennt, ohne Leerzeichen]

    andacht,bibel,väter,mütter,eltern,leseplan,christlich,gebet,familie,glaube,hörbuch,vorlesen

Der Name der App („Faithful parents") und der Untertitel werden von der Suche
ohnehin erfasst — sie gehören nicht in die Schlüsselbegriffe. „vaterschaft" und
„hebräisch" sind für „hörbuch" und „vorlesen" gewichen: Wer eine Andacht zum
Hören sucht, findet die App jetzt auch.

## Support-URL

    https://revelation-today.github.io/parents/

## Marketing-URL (optional)

    https://revelation-today.github.io/parents/

## Neue Funktionen in dieser Version

Wenn 1.0 noch nicht veröffentlicht ist:

    Erste Version.

Wenn schon eine Version im Store ist:

    Jetzt auch auf Deutsch: „Wie ein Vater" und „Wie eine Mutter tröstet", alle 62 Tage, mit Leseplänen und aufgenommener Lesung. Die App folgt der Sprache deines Geräts; umstellen kannst du sie unter „Über".

---

# Teil 4 — Eine Sprache in App Store Connect hinzufügen

Sprachen hängen an zwei Stellen, und beide müssen gefüllt werden:

1. **App-Informationen** (gilt für alle Versionen): Name, Untertitel,
   Datenschutzrichtlinie-URL.
2. **Die Version** (hier 1.0): Werbetext, Beschreibung, Schlüsselbegriffe,
   Support-URL, Marketing-URL, Neue Funktionen, Screenshots.

**So geht es:**

1. App Store Connect → *Apps* → **Faithful parents**.
2. Links *Vertrieb* („Distribution") wählen, dann in der Seitenleiste
   **App-Informationen** oder die Version **1.0 Bereit zur Einreichung**.
3. Oben rechts auf der Seite steht ein Sprachmenü (z. B. „Englisch (UK)").
   Aufklappen → **Sprache hinzufügen** → *Deutsch* → hinzufügen.
4. Die Seite zeigt jetzt die leeren deutschen Felder. Text aus Teil 3 einsetzen.
5. Screenshots: entweder dieselben hochladen oder leer lassen — leer bedeutet,
   dass der Store die der Primärsprache zeigt.
6. **Sichern** (oben rechts). Jede Sprache wird einzeln gesichert.

**Was dabei zu wissen ist:**

- Der deutsche Eintrag erscheint für alle, deren App Store auf Deutsch steht,
  nicht nur in Deutschland — auch Österreich und die Schweiz.
- Die Schlüsselbegriffe sind pro Sprache getrennt. Ohne deutsche
  Schlüsselbegriffe findet niemand die App mit „Andacht" oder „Leseplan".
- Eine Sprache lässt sich vor der Einreichung wieder entfernen (im selben Menü);
  ist die Version veröffentlicht, geht das erst mit der nächsten Version.
- Weitere Sprachen später (z. B. Indonesisch, Türkisch) laufen genauso. Sinnvoll
  ist das erst, wenn die Texte der App selbst in der Sprache vorliegen – wie jetzt beim
  Deutschen.
