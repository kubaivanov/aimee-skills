## Proč vaše AI píše obecné fráze a jak to změnit správnými daty

Znáte ten pocit frustrace? Ladíte svůj prompt k dokonalosti, přidáváte instrukce „buď víc kreativní", zkoušíte různé magické formulace, ale výsledek je pořád takový... nemastný neslaný. Texty jsou plné klišé a celé to působí jako šedý průměr.

Máme pro vás možná nepříjemnou pravdu: Chyba pravděpodobně není ve vašem promptu. Chyba je v kontextu, který jste AI (ne)dali.

Zatímco většina lidí řeší, jak se ptát (tzv. Prompt Engineering), ti pokročilejší z nich řeší, co a jak do AI dávají (Context Management).

Platí zde totiž jednoduchá rovnice: Průměrný prompt + Skvělý kontext = Velmi dobrý výsledek Geniální prompt + Žádný kontext = Průměrný výsledek

## Konec obecných frází a halucinací

Představte si AI jako skvělého kuchaře. Je to mistr svého řemesla. Ale když mu nedáte kvalitní suroviny, michelinské menu vám z nich zkrátka neuvaří.

Když do ChatGPT (nebo jiného AI nástroje) nevložíte dostatečný kontext, nutíte ho vařit z vody (respektive z jeho obecných tréninkových dat). Dá vám průměrnou odpověď, která sedí na 90 % firem, ale na žádnou z nich dokonale. Právě nedostatek kontextu je nejčastějším důvodem tzv. halucinací AI, kdy si model začne vymýšlet fakta, aby zaplnil prázdná místa.

Pokud chcete výstup, který řeší váš problém, vaši strategii a mluví vaším jazykem, musíte otevřít spíž s top surovinami. Musíte AI pustit ke svým datům.

## Kde brát data pro AI? Všechno může být součástí promptu

Co všechno může být tím „zlatým kontextem"? Skoro cokoliv digitálního, co ve firmě máte. Neomezujte se jen na text. Příprava dat pro AI může zahrnovat:

Screenshoty: AI má oči. Vyfoťte web, který se vám líbí. Vyfoťte nepřehledný graf z Analytics. Vyfoťte rozpracovaný design ve Figmě.

Přepisy hovorů: Toto je podceňovaný zlatý důl. Místo abyste AI složitě popisovali, co klient chce, dejte jí přečíst doslovný přepis vašeho callu nebo i vlákno mailové komunikace. „Tady je přepis stížnosti klienta. Napiš mu empatickou odpověď."

Interní dokumenty: PDFka, staré strategie, e-maily, brand manuály, prezentace.

Webové odkazy: Dokumentace k softwaru, články, inspirativní weby.

## Jak data připravit: Čistota dat je polovina úspěchu

Tady dělá chybu většina začátečníků. Vezmou dokument, zkopírují ho (CTRL+C) a „hodí" ho do chatu (CTRL+V). Často i s reklamami, patičkami, právními doložkami a balastem.

AI má omezenou pozornost (tzv. kontextové okno). Když ho zaplníte šumem, nezbyde jí kapacita na chytrou odpověď. Je to jako byste kuchaři dali bednu zeleniny i s hlínou a kořeny.

💡 Tip: Zamilujte si Markdown. AI modely milují strukturu. Formát .md (jednoduché značky jako # pro nadpisy a - pro odrážky) je pro ně jako mateřský jazyk. Než dáte AI číst článek z webu, „vyčistěte" ho. Odstraňte menu, reklamy a patičky. Nechte jen čistý text a strukturu. Čím čistší vstup, tím přesnější výstup.

Dobrá zpráva je, že i s čištěním dat vám může AI. V Aibility například používáme asistenta, který vezme audio přepis webináře a vyčistí ho od časových značek, výplňových slov, duplicit nebo přeřeků.

## Mini případová studie: Jak vzniká web díky kombinaci různých dat

Pojďme si to ukázat v praxi. Chcete navrhnout texty pro nový web. Líbí se vám struktura webu Lyssna, ale chcete tam mít svůj obsah.

Špatný postup: Napíšete do chatu: „Podívej se na web Lyssna a navrhni mi něco podobného pro moji firmu." Výsledek: AI bude hádat. Vymyslí si něco, co možná připomíná originál, ale bude to plytké a k ničemu.

Správný postup (s využitím kontextu):

Stáhnu data: Pomocí nástroje (např. Firecrawl) stáhnu textový obsah webu Lyssna.

Vyčistím: Odstraním balast, nechám jen strukturu nadpisů a sekcí (ideálně v Markdownu).

Dodám svůj kontext: Přidám dokument „O nás.pdf", kde popisuji svůj produkt a tón komunikace.

Spojím to: Prompt zní: „Vezmi strukturu webu Lyssna (Kontext A) a naplň ji mým obsahem (Kontext B). Zachovej psychologii prodeje a rozložení prvků, ale mluv o mém produktu."

Výsledek: Dostanete návrh webu, který má skvělou strukturu, ale s vašimi daty.

## Staňte se kurátorem informací

Vaše role v době AI se mění. Už nejste jen ten, kdo vymýšlí otázky. Stáváte se kurátorem informací. Váš úkol je najít ta správná data, vyčistit je a předložit je AI ve správný moment.

Přestaňte trávit hodiny laděním promptů. Začněte trávit minuty přípravou podkladů. Uvidíte, že AI najednou „zmoudří" a přestane vařit z vody.

## Často se ptáte

### Jak často bych měl/a AI používat, aby mi to opravdu pomáhalo?

Ideálně denně. Cílem je mít AI po ruce jako parťáka, ne jako nástroj, který otevřete jednou za týden. Vyhraďte si minimálně hodinu týdně na hlubší práci s AI a postupně zvyšujte frekvenci.

### Která AI je nejlepší na texty?

Záleží na úkolu. ChatGPT je univerzální a nejrozšířenější. Claude často dává lidštější výsledky. Gemini exceluje v práci s obrázky. Doporučujeme udělat „mini-výběrko" – zkusit stejný úkol ve více nástrojích a vybrat nejlepší výsledek.

### Stačí bezplatná verze, nebo se vyplatí platit?

Free verze vás bude limitovat rychleji, než čekáte. Doporučujeme vyzkoušet placenou verzi alespoň na měsíc (cca 500 Kč). Rozdíl v kvalitě odpovědí a rychlosti je znatelný.

### Jsou moje data v bezpečí?

U bezplatných verzí se data mohou používat k trénování modelů. Placené tarify (Team, Enterprise) mají tuto funkci vypnutou nebo ji lze vypnout. Vždy konzultujte s IT oddělením. Microsoft Copilot ve firemním prostředí je považován za bezpečný.

### Co dělat, když se zaseknu a nevím, jak dál?

Zeptejte se přímo AI. Napište: „Nevím, jak tohle udělat. Dej mi návod krok za krokem, polopaticky." Když narazíte na chybu, pošlete do chatu screenshot. AI vám pomůže ji vyřešit.

### Musím umět promptovat, nebo stačí používat hotové GPTs asistenty?

Hotové GPTs (předpřipravení asistenti) jsou skvělá zkratka pro rutinní úkoly. Ale nemusí vždy sedět vašim konkrétním potřebám a postupům. Proto je důležité chápat základní principy promptování. Dokážete si díky tomu tvořit vlastní asistenty nebo se ptát AI tak, aby vám dávala opravdu kvalitní výsledky.







