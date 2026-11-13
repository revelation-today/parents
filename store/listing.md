# App Store-Eintrag — Faithful parents

Die Feldnamen stehen so, wie App Store Connect sie auf Deutsch zeigt.
Zeichengrenzen in eckigen Klammern.

Die App gibt es **auf zehn Sprachen**: Englisch (*Like a Father* / *As a Mother Comforts*),
Deutsch (*Wie ein Vater* / *Wie eine Mutter tröstet*), Spanisch, Französisch, Portugiesisch,
Türkisch, Russisch, Koreanisch, Vietnamesisch und Indonesisch. Sie folgt der Sprache des Geräts und lässt sich unter
*About/Über* umstellen. Die Primärsprache des Eintrags bleibt Englisch (UK); der deutsche
Eintrag (Teil 3) und die acht weiteren (Teil 3b) beschreiben die jeweilige Ausgabe.

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
International Version (Anglicised). Alle anderen Ausgaben (Deutsch, Spanisch, Französisch,
Portugiesisch, Türkisch, Russisch, Koreanisch, Vietnamesisch, Indonesisch) zitieren nur eigene Übersetzungen des Autors und
enthalten keine Inhalte Dritter. Antwort:

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
                             (nur ein optionaler Link zum Bibeltext: bibleserver.com auf
                             Deutsch, bible.com/YouVersion auf Türkisch, sonst
                             BibleGateway.com)
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
                               (je Sprache …/parents/privacy-<code>.html, z. B. privacy-de.html,
                               privacy-es.html, privacy-fr.html, privacy-pt.html, privacy-tr.html,
                               privacy-ru.html, privacy-ko.html, privacy-vi.html, privacy-id.html — die deutsche Fassung ist die
                               rechtlich verbindliche; erzeugt mit tools/app/make_privacy.py)
    Datenerfassung:            „Es werden keine Daten von dieser App erfasst."

    Keine Accounts, keine Analyse, keine Werbung, kein Tracking.
    Lesefortschritt und Einstellungen bleiben auf dem Gerät.

## Hinweise für die App-Prüfung (App-Prüfungsinformationen → Anmerkungen)

„Anmeldung erforderlich" bleibt **aus** — die App hat keinen Login.

    This is a self-contained reading app, not a wrapper around a website.

    • All text — two complete 31-day devotionals, 62 readings, in English, German, Spanish, French, Portuguese, Turkish, Russian, Korean, Vietnamese and Indonesian — is
      bundled in the app. It works with the device in airplane mode; please feel free to test it
      that way. The app follows the device language; About → Language switches it.
    • Read aloud: recorded narration is streamed from the app's own website
      (revelation-today.github.io/parents) and can be downloaded for offline listening; without
      a connection the app reads with the device's built-in voice. Recorded narration exists in eight of the ten languages (not Vietnamese or Indonesian); the device voice is the fallback and the only voice in those two.
    • The app has no accounts and no server. Reading plans, progress, marked days and
      text size are stored on the device.
    • The only outbound link is optional: on each day, "Read <passage>" opens that Bible
      passage in the browser (BibleGateway.com in most languages, bibleserver.com in German, bible.com in Turkish), for
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

    Die Screenshots zeigen die englische App. Für alle weiteren Sprachen gilt dasselbe
    (leer lassen = Screenshots der Primärsprache). Für den deutschen Eintrag sind deutsche
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
    • When Parents Fall Short — 8 days
    • Grief and Loss — 7 days
    • What You Carry from Home — 7 days

    A plan never runs away from you. Miss a week, and it waits where you left off.

    HONEST ABOUT THE HARD PARTS

    These books do not skip the texts people find difficult: the rod sayings in Proverbs, the daughters, the fathers who did harm, and the readers whose own parents hurt them. Where scholars disagree, the notes say so.

    BUILT FOR READING

    • Works completely offline. Nothing to sign in to, no account, no advertising.
    • Your reading progress stays on your device.
    • Light and dark, and text you can make bigger.

    Both devotionals rest on published biblical scholarship, and the notes name the works behind each day.

    Also in German (Wie ein Vater, Wie eine Mutter tröstet), Spanish, French, Portuguese, Turkish, Russian, Korean, Vietnamese and Indonesian. The app follows your device's language.

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
Vorlesefunktion. Der Store-Name ist „Treue Eltern im Glauben"; der Name unter dem Symbol auf dem Handy bleibt
„Faithful parents" (capacitor.config.json). Untertitel und Beschreibung sind deutsch und nennen die deutschen Buchtitel.

## Name [30]

    Treue Eltern im Glauben

## Untertitel [30]

    Andachten für Väter und Mütter

## Werbetext [170]

    Zwei Andachtsbücher über die Väter und Mütter der Bibel, je 31 Tage – mit Leseplänen, dem hebräischen Wort des Tages, Quellen und Vorlesen. In zehn Sprachen.

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
    • Wenn Eltern an Grenzen stoßen – 8 Tage
    • Trauer und Verlust – 7 Tage
    • Was du von zu Hause mitträgst – 7 Tage

    Kein Plan läuft dir davon. Verpasst du eine Woche, wartet er dort, wo du aufgehört hast.

    ZUM HÖREN

    Jeder Tag kann vorgelesen werden – von einer aufgenommenen Stimme oder von der Stimme deines Geräts. Der Text läuft beim Vorlesen mit, und ein Tipp auf einen Absatz springt dorthin. Die Lesungen lassen sich für unterwegs aufs Gerät laden.

    EHRLICH BEI DEN SCHWEREN STELLEN

    Diese Bücher lassen die schwierigen Texte nicht aus: die Rute in den Sprüchen, die Töchter, die Väter, die Schaden angerichtet haben, und die Leser, denen die eigenen Eltern wehgetan haben. Wo die Forschung uneins ist, sagen es die Anmerkungen.

    ZUM LESEN GEBAUT

    • Die Texte funktionieren vollständig offline. Keine Anmeldung, kein Konto, keine Werbung.
    • Dein Lesefortschritt bleibt auf deinem Gerät.
    • Hell und dunkel, und Text, den du größer stellen kannst.
    • Auch auf Englisch, Spanisch, Französisch, Portugiesisch, Türkisch, Russisch, Koreanisch, Vietnamesisch und Indonesisch – die App folgt der Sprache deines Geräts und lässt sich umstellen.

    Beide Bücher stützen sich auf veröffentlichte Bibelwissenschaft; die Anmerkungen nennen die Werke hinter jedem Tag. Die Bibelzitate der deutschen Ausgabe sind eigene Übersetzungen aus dem Hebräischen und Griechischen.

## Schlüsselbegriffe [100, mit Komma getrennt, ohne Leerzeichen]

    andacht,bibel,väter,mütter,eltern,leseplan,christlich,gebet,familie,glaube,hörbuch,vorlesen

Der Name der App („Treue Eltern im Glauben") und der Untertitel werden von der Suche
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

# Teil 3b — Die weiteren Sprachen (es, fr, pt, tr, ru, ko, vi, id)

Die App ist seit 1.1 (oder der Version, die sie zuerst enthält) auch auf Spanisch, Französisch,
Portugiesisch, Türkisch, Russisch, Koreanisch, Vietnamesisch und Indonesisch vollständig: beide Bücher, alle 62 Tage, Quiz,
Lesepläne, Oberfläche. Der Store-Name ist je Sprache übersetzt (unter „Name" jedes Abschnitts); der Name unter dem Symbol auf dem Handy bleibt überall „Faithful parents". Alle Bibelzitate sind
eigene Übersetzungen des Autors aus dem Hebräischen und Griechischen (keine Inhalte Dritter).

**Vorlesen:** Für es, fr, pt, ru, tr und ko gibt es seit November 2026 eine **aufgenommene Lesung**
(es, pt: Kokoro „Dora"; fr: Kokoro „Siwis"; ru: Piper „Dmitri", CC0; tr: Piper „dfki" und
ko: Piper „kss" — beide CC BY-NC-SA 4.0, nur nicht-kommerziell: die App muss kostenlos und
werbefrei bleiben und nennt die Quellen unter *About*). Vietnamesisch und Indonesisch
haben keine aufgenommene Lesung, nur die Stimme des Geräts.

**Vor der Einreichung:** Die Texte sind maschinell übersetzt und noch von keiner
Muttersprachlerin und keinem Muttersprachler gegengelesen. Beschreibung und Schlüsselbegriffe
ebenso — bitte vor dem Absenden jede Sprache einmal prüfen lassen.

Store-Sprachen in App Store Connect: *Spanisch (Spanien)*, *Französisch*, *Portugiesisch (Brasilien)*,
*Türkisch*, *Russisch*, *Koreanisch*, *Vietnamesisch*, *Indonesisch*. (Wer Spanisch für Lateinamerika möchte, fügt zusätzlich
*Spanisch (Mexiko)* mit demselben Text hinzu.) Datenschutz-URL je Sprache:
`https://revelation-today.github.io/parents/privacy-<es|fr|pt|tr|ru|ko|vi|id>.html`.

---

## Spanisch (es)

### Name [30]

    Padres fieles

### Untertitel [30]

    Devocional para padres

### Werbetext [170]

    Dos devocionales de treinta y un días sobre los padres y las madres de la Biblia, con planes de lectura, la palabra hebrea del día, fuentes y lectura en voz alta.

### Beschreibung [4000]

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
    • Cuando los padres se quedan cortos — 8 días
    • Duelo y pérdida — 7 días
    • Lo que llevas de tu hogar — 7 días

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

### Schlüsselbegriffe [100]

    devocional,biblia,padres,madres,familia,oración,plan de lectura,cristiano,diario,fe,hebreo,lectura

---

## Französisch (fr)

### Name [30]

    Parents fidèles

### Untertitel [30]

    Méditations pour parents

### Werbetext [170]

    Deux livres de méditation de trente et un jours sur les pères et les mères de la Bible, avec plans de lecture, le mot hébreu du jour, sources et lecture à voix haute.

### Beschreibung [4000]

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
    • Quand les parents n'y arrivent pas — 8 jours
    • Deuil et perte — 7 jours
    • Ce que tu portes de ton foyer — 7 jours

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

### Schlüsselbegriffe [100]

    méditation,bible,pères,mères,parents,famille,prière,plan de lecture,chrétien,quotidien,foi,hébreu

---

## Portugiesisch (pt, Brasilien)

### Name [30]

    Pais fiéis

### Untertitel [30]

    Devocional para pais e mães

### Werbetext [170]

    Dois devocionais de trinta e um dias sobre os pais e as mães da Bíblia, com planos de leitura, a palavra hebraica do dia, fontes e leitura em voz alta.

### Beschreibung [4000]

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
    • Quando os pais ficam aquém — 8 dias
    • Luto e perda — 7 dias
    • O que você carrega do seu lar — 7 dias

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

### Schlüsselbegriffe [100]

    devocional,bíblia,pais,mães,família,oração,plano de leitura,cristão,diário,fé,hebraico,leitura

---

## Türkisch (tr)

### Name [30]

    Sadık Ebeveynler

### Untertitel [30]

    Ebeveynler için günlük okuma

### Werbetext [170]

    Kutsal Kitap’ın babaları ve anneleri üzerine otuz bir günlük iki kitap: okuma planları, günün İbranice sözcüğü, kaynaklar ve kayıtlı sesli okuma.

### Beschreibung [4000]

    Tek uygulamada otuz bir günlük iki kitap: Kutsal Kitap’ın babalarını anlatan Bir Baba Gibi ve annelerini anlatan Bir Anne Avuttuğu Gibi. Birini oku, ötekini oku ya da ikisini yan yana oku.

    Kutsal Kitap’ın ebeveynleri bir kahramanlar galerisi değildir. İbrahim oğlunun üzerine bıçağı kaldırır. Eli oğullarını engellemez. Davut çok geç ağlar. Sara bir cariyeyi çöle sürer; Rebeka kocasını aldatır; Rahel ile Lea çocuklarının adları üzerinden çekişir. Yanlarında dua eden Hanna; ölü oğullarını aylarca bekleyen Rispa; küçük bir sepet yapan Yokebed; denetleyemediği çocukları için dua eden Eyüp; “nasıl” diye soran Manoah; ve Luka 15’teki koşan baba.

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
    • Anne babalar yetersiz kaldığında — 8 gün
    • Yas ve kayıp — 7 gün
    • Evinden taşıdıkların — 7 gün

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

### Schlüsselbegriffe [100]

    günlük okuma,kutsal kitap,baba,anne,aile,dua,okuma planı,hristiyan,iman,İbranice,sesli okuma

---

## Russisch (ru)

### Name [30]

    Верные родители

### Untertitel [30]

    Размышления для родителей

### Werbetext [170]

    Две книги на тридцать один день об отцах и матерях Библии: планы чтения, древнееврейское слово дня, источники и чтение вслух в записи.

### Beschreibung [4000]

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
    • Когда родители не справляются — 8 дней
    • Горе и утрата — 7 дней
    • То, что ты несёшь из родного дома — 7 дней

    План никогда не убегает от вас. Пропустите неделю — он ждёт там, где вы остановились.

    ЧЕСТНО О ТРУДНОМ

    Эти книги не обходят места, которые считают трудными: изречения о розге в Притчах, дочерей, отцов, причинивших вред, и читателей, которых ранили собственные родители. Где учёные расходятся, примечания говорят об этом.

    СОЗДАНО ДЛЯ ЧТЕНИЯ

    • Работает полностью без сети. Без входа, без аккаунта, без рекламы.
    • Ваш прогресс чтения остаётся на вашем устройстве.
    • Светлая и тёмная темы, текст можно увеличить.
    • Каждый день можно прослушать в записи или голосом вашего устройства; записи можно скачать для прослушивания без сети.

    Обе книги опираются на опубликованные библейские исследования, а примечания называют труды, стоящие за каждым днём. Библейские цитаты русского издания — собственные переводы автора с древнееврейского и греческого.

    Есть также на английском, немецком, испанском, французском, португальском, турецком и корейском. Приложение следует языку вашего устройства.

### Schlüsselbegriffe [100]

    размышления,библия,отцы,матери,родители,семья,молитва,план чтения,христианство,вера,иврит

---

## Koreanisch (ko)

### Name [30]

    신실한 부모

### Untertitel [30]

    부모를 위한 묵상

### Werbetext [170]

    성경 속 아버지와 어머니를 다룬 서른하루짜리 묵상집 두 권. 읽기 계획, 오늘의 히브리어 단어, 출처, 녹음된 낭독까지 한 앱에 담았습니다.

### Beschreibung [4000]

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
    • 부모가 부족할 때 — 8일
    • 슬픔과 상실 — 7일
    • 집에서 안고 온 것들 — 7일

    계획은 결코 당신을 앞서 달아나지 않습니다. 한 주를 건너뛰어도 멈춘 자리에서 기다립니다.

    어려운 대목도 정직하게

    이 책들은 사람들이 어렵게 여기는 본문을 건너뛰지 않습니다. 잠언의 매에 관한 말씀, 딸들, 해를 끼친 아버지들, 그리고 자기 부모에게 상처받은 독자들을 다룹니다. 학자들의 견해가 갈리는 곳은 주석이 그렇게 밝힙니다.

    읽기 위해 만들었습니다

    • 인터넷 없이도 완전히 작동합니다. 로그인도 계정도 광고도 없습니다.
    • 읽기 진행 상황은 기기에 남습니다.
    • 밝은 화면과 어두운 화면, 키울 수 있는 글자.
    • 날마다의 글을 녹음된 음성이나 기기의 음성으로 들을 수 있고, 내려받아 오프라인으로도 들을 수 있습니다.

    두 책 모두 출판된 성경 연구에 기대고 있으며, 주석은 날마다의 근거 저작을 밝힙니다. 한국어판의 성경 인용은 저자가 히브리어와 헬라어에서 직접 옮긴 번역입니다.

    영어, 독일어, 스페인어, 프랑스어, 포르투갈어, 터키어, 러시아어로도 볼 수 있습니다. 앱은 기기의 언어를 따릅니다.

### Schlüsselbegriffe [100]

    묵상,성경,아버지,어머니,부모,가정,기도,읽기 계획,기독교,신앙,히브리어,큐티

---

## Vietnamesisch (vi)

### Name [30]

    Cha mẹ trung tín

### Untertitel [30]

    Suy niệm cho cha và mẹ

### Werbetext [170]

    Hai cuốn sách suy niệm ba mươi mốt ngày về những người cha và người mẹ trong Kinh Thánh: kế hoạch đọc, từ Hê-bơ-rơ của ngày, nguồn tham khảo và đọc thành tiếng.

### Beschreibung [4000]

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
    • Khi cha mẹ chưa làm tròn — 8 ngày
    • Đau buồn và mất mát — 7 ngày
    • Điều bạn mang theo từ mái nhà — 7 ngày

    Kế hoạch không bao giờ bỏ rơi bạn. Nếu một tuần trôi qua, nó vẫn chờ ở chỗ bạn dừng lại.

    THẲNG THẮN VỚI NHỮNG PHẦN KHÓ

    Hai cuốn sách này không bỏ qua những đoạn mà người ta thấy khó: những câu nói về cây roi trong Châm Ngôn, các cô con gái, những người cha đã gây tổn hại, và những độc giả đã bị chính cha mẹ mình làm tổn thương. Ở chỗ các học giả bất đồng, phần ghi chú sẽ nói rõ.

    LÀM RA ĐỂ ĐỌC

    • Hoạt động hoàn toàn khi không có mạng. Không đăng nhập, không tài khoản, không quảng cáo.
    • Tiến trình đọc của bạn nằm trên thiết bị của bạn.
    • Nền sáng và tối, và chữ có thể phóng to.
    • Có thể đọc thành tiếng từng ngày bằng giọng của thiết bị.

    Hai cuốn sách suy niệm này dựa trên các nghiên cứu Kinh Thánh đã được công bố, và phần ghi chú nêu các công trình đứng sau từng ngày. Các đoạn trích Kinh Thánh trong bản tiếng Việt là bản dịch riêng của tác giả từ tiếng Hê-bơ-rơ và tiếng Hy Lạp.

    Cũng có bằng tiếng Anh, tiếng Đức, tiếng Tây Ban Nha, tiếng Pháp, tiếng Bồ Đào Nha, tiếng Thổ Nhĩ Kỳ, tiếng Nga và tiếng Hàn. Ứng dụng theo ngôn ngữ của thiết bị bạn.

### Schlüsselbegriffe [100]

    suy niệm,kinh thánh,cha,mẹ,gia đình,cầu nguyện,kế hoạch đọc,cơ đốc,hằng ngày,đức tin,hê-bơ-rơ

---

## Indonesisch (id)

### Name [30]

    Orang Tua Setia

### Untertitel [30]

    Renungan untuk ayah dan ibu

### Werbetext [170]

    Dua buku renungan tiga puluh satu hari tentang para bapa dan ibu dalam Alkitab, dengan rencana baca, kata Ibrani hari ini, dan sumberan.

### Beschreibung [4000]

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
    • Ketika orang tua belum mampu — 8 hari
    • Duka dan kehilangan — 7 hari
    • Yang Anda bawa dari rumah — 7 hari

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

### Schlüsselbegriffe [100]

    renungan,alkitab,bapa,ibu,keluarga,doa,rencana baca,kristen,harian,iman,ibrani,orang tua

---

# Teil 4 — Eine Sprache in App Store Connect hinzufügen

Sprachen hängen an zwei Stellen, und beide müssen gefüllt werden:

1. **App-Informationen** (gilt für alle Versionen): Name, Untertitel,
   Datenschutzrichtlinie-URL. Für Deutsch: `https://revelation-today.github.io/parents/privacy-de.html`.
2. **Die Version** (hier 1.0; bei den neuen Sprachen die Version, die sie zuerst enthält — iOS-Build-Version höher als die letzte hochgeladene wählen): Werbetext, Beschreibung, Schlüsselbegriffe,
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
- Weitere Sprachen später (z. B. Arabisch) laufen genauso; die acht aus Teil 3b ebenfalls. Sinnvoll
  ist das erst, wenn die Texte der App selbst in der Sprache vorliegen – wie jetzt beim
  Deutschen.
