Zde je vyčištěný přepis webináře.

**Co jsem udělal:**
1.  **Odstranění technického šumu:** Vymazal jsem všechny časové značky (`[01:59]`), informace o výpadku Zoomu na začátku a opakující se organizační vsuvky.
2.  **Oprava transkripčních chyb:** Text obsahoval velké množství fonetických zkomolenin technických pojmů. Opravil jsem je následovně:
    *   "Elomko/Elalonka" → **LLMko** (Large Language Model)
    *   "Prumpování/Pruntování" → **Promptování**
    *   "Tonovoce/Tonovu" → **Tone of Voice**
    *   "Margdal/Margawn/Margdam" → **Markdown**
    *   "Fuship prompting" → **Few-shot prompting**
    *   "Brom chaing" → **Prompt chaining**
    *   "Kontext i Skincare" → **Context is King**
    *   "Farnostiklad farerkrow" → **Firecrawl** (nástroj na scraping)
    *   "Bez prepreticis" → **Best practices**
3.  **Stylistická úprava:** Odstranil jsem nadměrné koktání ("er, no, jako, prostě"), spojil roztrhané věty a rozdělil text do logických odstavců pod nadpisy pro lepší čitelnost.
4.  **Zachování obsahu:** Všechny myšlenky, příklady (i ty s "Amy") a Q&A sekce zůstaly zachovány.

---

# Pokročilé promptování Naučte se mluvit s AI jako expert - 20.10.2025 - vyčištěný.md

## Úvod a představení

**Aibility | Petra Květová Pšeničná:** Krásné ráno. Já vás vítám na dnešním webináři, na kterém se podíváme, jak na promptování. Ráda bych na začátku řekla, kdo jsme a co děláme. Pokud jste se k nám připojili dnes poprvé, jsme tým Aibility a získáváte díky nám superschopnosti v oblasti umělé inteligence.

Dovolte mi, abych se představila. Jmenuju se Petra Květová Pšeničná. Provedu vás dnešním webináři spolu s lektorem, ke kterému se dostaneme za chvíli. Jsem moderátorka Aibility a AI EduStream. Pokud jste s námi v AI Edu, tak se potkáváme pravidelně. Zároveň jsem moderátorka podcastů, různých konferencí a spoluzaložila jsem neziskovku Fandi mámám, která pomáhá samoživitelkám.

Co nás dnes čeká? Webinář na téma „Pokročilé promptování: Naučte se mluvit s AI jako expert“. Obsah bude velmi praktický. Podíváme se na to, proč AI neposlouchá, jaké nejčastější chyby děláme v promptech, jak rychle poznat, že jsme prompt zadali špatně, a případně jak to opravit. Taky se podíváme na to, jak zásadní je kontext a role pro promptování, abyste dostali správný výstup. Ukážeme vám šablony, které mohou šetřit čas, a ověřené prompty. Bude čas i na živé ukázky v akci, protože to je to nejcennější, co si můžete z webináře odnést – vyzkoušet si to sami.

Nyní už k tomu, kdo je dnešním hostem. Webinářem nás provede Tom Paulus. Hezký den, Tome, vítám tě.

**Tom Paulus:** Ahoj, děkuji pěkně. Mám ve zvyku se na začátku takovýchto webinářů představovat, abyste věděli, co je to za „mluvící hlavu“, která na vás bude mluvit nejbližší hodinu a půl. Jsem Tomáš, Service Designer. Dlouhé roky jsem táta, jsem tvůrce. Rozhodně nejsem programátor ani technicky založený člověk. Aktuálně v Aibility tvořím „Anabolic“, což je fitko poháněné AI. Zní to hrozně marketingově, ale je to prostě fitko, kde máte AI trenéra.

Dvanáct let jsem designoval služby pro různé velké korporáty po Evropě. Dva roky dozadu jsem měl pocit, že moje práce trochu stagnuje, byla to nuda, všechno bylo stejné. A pak jsem objevil GPT-3.5. Začal jsem zjišťovat, že to může být zase zábava. Začal jsem jednoduchými věcmi – tvořit copy do designu ve Figmě, psát věci v mém Tone of Voice a zlepšovat své designové návrhy.

Přišel jsem na to, že opakující se věci můžu hodit do promptů a nemusím je dělat stále dokola. Zjistil jsem, že si nemusím platit za vizualizaci zákaznických cest drahé nástroje, které stojí tisíce dolarů ročně, ale můžu si nahrát přepisy z call centra a nechat si vizuálně vytvořit mapu. Přestal jsem si kupovat drobné apky a začal jsem si je vlastně tvořit sám.

Například moji kolegové v bývalé agentuře se bavili o problémech a já jsem jim tvořil řešení. Přišlo nám RFP od klienta, obrovský stostránkový dokument. Já jsem ho nahrál do bota a ono mi to vytvořilo aplikaci. Najednou se nám to naceňovalo mnohem jednodušeji. Časem jsem přišel na to, že abychom dokázali z těchto nástrojů dostávat dobré výstupy, potřebujeme fakt luxusní vstupy. A tak jsem se pustil do skriptování. Mojí pravou rukou je Cursor. Dokázal jsem spojovat dokumenty, generovat výstupy v různých formátech, psal jsem si rozšíření do Chromu a od toho všeho byl jen krok k agentům.

Když si například někdo koupí můj e-book, chystá se mu automatizace a reálně personalizovaná zpráva na základě jeho posledních LinkedIn postů. Začal jsem „type-codovat“ a ani jsem nevěděl, že se to tak jmenuje. Když jsem chystal tento webinář, uvědomil jsem si, že celá tato moje cesta měla společnou jednu věc: byla založena na dobrých promptech.

## Prompt jako komunikační médium

**Tom Paulus:** Prompt je vlastně komunikační médium se softwarem, s AI, s LLM modelem. Já vám dnes zkusím ukázat, jak si tuto komunikaci vyladit tak, aby vám ty modely rozuměly. Ukážu vám nástroje, které si myslím, že jsou skvělé. Jeden z nich vám pomůže vytvořit jakýsi „ekosystém promptů“. Myslím si, že je lepší vás naučit rybařit, než po vás házet ryby.

Zajímalo by mě, co byste vlastně chtěli vytvořit? Jaký prompt potřebujete? Zkuste to napsat do chatu.

*(Tom čte reakce z chatu)*
Vidím tady: „Potřebuji prompt, který za mě udělá práci na celý rok.“ Spoiler alert: takový prompt neexistuje. Ale ukážu vám, jak si nastavit různé prompty, aby to k tomu aspoň trošku směrovalo. Dále vidím: „Posunout se s agenty“, „Čemu se vyhnout“, „Prompty pro GPT, Claude, Cursor“. Super, k tomu se dnes dostaneme.

Jak jsem říkal, prompt je komunikační médium. Ta komunikace může vypadat různě. Může to vypadat tak, že se budete vašim asistentům zdravit „Čauky mňauky“ a oni se budou zdravit vám. Ale můžete k asistentům přistupovat tak, že jim řeknete: „Hele, pochop, že já to nechci dělat. Chci napsat jeden příkaz a ty to uděláš za mě. Nebudu ti nic zadávat víckrát.“

Někdy můžete být i drsnější, když jste frustrovaní. Mám tu ukázku, kdy jsem si tvořil texty na web a asi po dvaceti minutách jsem nedostával dobré výstupy, tak jsem musel být drsnější. Ty lepší a komplexnější prompty jsou skutečně složité. Nějakou dobu dozadu unikly systémové prompty obrovského množství služeb, například Claude, Perplexity, Notion AI. Ty prompty mohou mít klidně tisíc, dvanáct set řádků a popisují velmi specifickým způsobem, co ten agent má dělat.

Je dobré si říct, že já sám používám hodně složité prompty v momentě, kdy potřebuji dělat jednu velmi specifickou věc a velmi mi na ní záleží. Ale zároveň často používám prompty typu: „Udělej mi z toho text, udělej XYZ.“ A je to v pořádku. Je to stejné, jako když vedle mě sedí kolega, se kterým dělám dvacet let – řeknu mu to jednou větou. Versus když mám juniora, kterému to musím popsat krok za krokem. Ne na všechno potřebujete extrémně složitý prompt podle nejlepších best practices.

## Struktura dobrého promptu

**Tom Paulus:** Jak vypadá dobré zadání? Měli bychom být schopni:
1.  Popisovat velmi přesně zadání.
2.  Rozdělit úkol na konkrétní části a kroky.
3.  Obohatit ho o kontext.
4.  Dát LLMku nějakou roli (roli experta).
5.  Přidat formát výstupu.
6.  Dokola testovat a iterovat.

Málokdy to dopadne tak, že si vytvoříte jeden prompt a s ním budete žít do konce života. Velmi často budete muset iterovat, hlavně u promptů pro asistenty nebo do GPT projektů.

### 1. Přesné zadání
Ukážu vám to na příkladu promptu, který mi pomáhá psát webinář. Snažím se velmi přesně popsat, že od něj potřebuji, aby se mě nejdřív zeptal, o čem ten webinář má být, jaký má být cíl, jaký je hlavní topic. Musím být schopen se jasně vyjadřovat. Příklad: „Co chci dosáhnout?“ Protože čím vágnější jsem já, tím vágnější odpovědi budou od LLMka.

### 2. Rozdělení na části
Zase u mého webinářového promptu mám jasně rozdělené fáze:
*   Fáze 1: Content Discovery (zjisti obsah).
*   Fáze 2: Vytvoř outline webináře (popiš v jasných bodech, jak to má vypadat).
*   Fáze 3: Pomoz mi tvořit slide po slidu.

### 3. Kontext
Čím víc kontextu dodáte, tím lepší výsledky budou. Když jsem brainstormoval obsah tohoto webináře, celé moje zadání byly tři screenshoty ze Slacku. To byl celý můj prompt na začátek. Nebo když jsem chtěl od GPT, aby mi pomohlo tvořit produkt na zpracování dat o uživatelích, nahrál jsem tři soubory s konkrétními daty.

Může to být i primitivní popis Tone of Voice, který dokola používám. Mám nadefinované, co znamená naše „Amy“ (náš AI asistent) a jak komunikuje. Potřebuji výstupy v tomto tónu, tak to všude připojuji.

### 4. Role
Většinou je to jedna větička: „Jsi expert na to a to“ nebo „Jsi designér, který pracuje v top tech firmách na světě, pracoval jsi pro Elona Muska a Apple a budeš tvořit design podle těchto guidelines.“

Proč to děláme? Pomůže to LLMku se správně nasměrovat v té obrovské databázi. LLMka jsou statistické modely. Když mu dobře zadefinujete roli a cíl, bude schopné se přesněji pohybovat v rozhodovacím stromě a dá vám relevantnější výsledek.

### 5. Formát výstupu
Pokud jste vágní, výstup bude vágní. Mám tu prompt pro reverzní inženýrství, kde mám přesně zadefinované, v jakém formátu chci výstup: „Zadej roli, vypiš tvůj cíl, konkrétní věci, Tone of Voice, formát, content.“

Může to být i složitější, kdy po asistentovi chci konkrétní JSON. Mám napsané, že musí vyprodukovat výstup pouze v tomto tvaru. Proč? Protože kdyby mi to dal v jiném formátu, zavádí tam nedeterminismus. Kdyby byl výstup pokaždé jiný, nemohl bych na něj navazovat v automatizacích.

### 6. Testování a iterace
Když vytvoříte prompt, udělejte s ním jednu otočku. Zjistěte, jaký výstup vám dal, vezměte ten výstup, hoďte ho zpátky do AI a zeptejte se: „Co udělal asistent na tom promptu špatně a jak ten prompt má vypadat jinak?“

Například jsem měl prompt, který koučoval lidi. Nahrával jsem do GPT celou konverzaci a ptal se na feedback: „Hele, co udělal ten můj asistent špatně na základě toho promptu?“

## Playbook pro promptování

**Tom Paulus:** Vytvořil jsem pro vás přehled, kde jsem vzal best practices pro promptování od OpenAI a od Claude (Anthropic) a nechal jsem Cursor, aby mi vytvořil „Playbook“. Odkaz dostanete. Tvořil jsem to tak, že jsem řekl Cursoru, aby stáhl obsah všech stránek z odkazů a vytvořil z toho playbook.

Sice vás učím, jak mají vypadat nejlepší prompty, ale není nutné je vždy používat. Podle typu úlohy volíte složitost promptu.

## Context is King

**Tom Paulus:** Někdo v chatu zmínil „Context is King“. To je přesné, hlavně v době LLM. Prompt engineering řeší, jak se správně ptát. Ale kontext řeší, jaké informace model potřebuje znát, aby odpověděl dobře. Pokud se budu spoléhat jen na to, co má model v paměti, snadno se zmýlí (halucinuje).

Jako kontext můžete používat cokoliv:
*   Screenshoty z webu, Slacku, sociálních sítí.
*   Odkazy (např. na dokumentaci v Make.com).
*   Přepisy rozhovorů (my nahráváme všechno, i offsite meetingy, a necháváme AI, aby nám to rozsekala na témata).

Například když budujeme Amy, máme vytvořené strategie, jak doporučujeme nástroje a jak pracovat s daty. Mám to uložené na Gitu. Můžu vzít tuto strategii a říct Cursoru: „Shrň mi to do jedné věty“ nebo „Uprav tooling strategii na úroveň startupu s pěti zaměstnanci a ulož to do nového souboru.“ On vezme informace, které už máme, zpracuje je a uloží.

### Jak získávat kontext (Demo)
Líbí se mi web *Lyssna Labs*. Chtěl bych, aby Amy měla podobný web.
1.  Použiji nástroj **Firecrawl** (nebo rozšíření v Cursoru), který stáhne obsah stránky.
2.  Stáhnu si Markdown, který mi Firecrawl vytvořil. Vidím, že je tam balast (odkazy, obrázky).
3.  Vezmu ten „zabordelený“ soubor, hodím ho do ChatGPT a řeknu: „Vyčisti tento Markdown tak, aby obsahoval jen strukturu webu s konkrétními texty a vypiš to do Canvasu.“
4.  GPT mi to vyčistí a připraví strukturu.
5.  Otevřu nový chat s GPT (kde už mám kontext o Amy díky paměti) a řeknu: „Vypiš všechno o Amy.“
6.  Teď mám dva kontexty: strukturu webu, která se mi líbí, a informace o Amy.
7.  Zadám prompt: „Jsi seniorní stratég/designér. Tady je kontext Amy, tady je referenční stránka. Vytvoř nový web na základě Lyssna Labs, ale s obsahem o Amy.“

Díky tomu vznikne web ve stejné struktuře, ale s mým obsahem. To byl jeden prompt a dvě kontextové informace.

## Dotazy z chatu

**Aibility | Petra Květová Pšeničná:** Tome, kdy použít spíš ChatGPT a kdy Cursor?

**Tom Paulus:** Cursor je pro mě zajímavý v tom, že krásně pracuje se soubory na disku a na některé věci umí vytvořit skripty bez využití LLM. Jsem si jistější, že si nebude vymýšlet. Zvládá běžet extrémně dlouho (třeba 36 hodin) na složité úlohy. Používám ho, když pracuji s daty, která potřebuji mít 100% ověřená (např. exporty plateb ze Stripe). Cursor také obsahuje GPT, je to vlastně wrapper na všechny modely. Navíc, jelikož pracuje s lokálními soubory, je to pro mě přenositelnější než mít vše v ChatGPT. Ale spousta lidí si vystačí s ChatGPT.

**Aibility | Petra Květová Pšeničná:** V jakém formátu nejlépe přikládat soubory? JSON, Markdown, PDF?

**Tom Paulus:** Strukturované formáty fungují dobře. Já používám **Markdown**, protože ho sám dobře přečtu a LLM ho čte mnohem lépe než PDF. **JSON** nebo **XML** je pro LLM možná ještě lepší, protože je extrémně strukturovaný. Můžete mít asistenta, který vám jakýkoliv soubor převede do Markdownu nebo JSONu. PDFka v nástrojích jako Botpress často dávají podprůměrné výsledky, takže doporučuji převádět do Markdownu.

**Aibility | Petra Květová Pšeničná:** Je lepší prompt v angličtině nebo v češtině?

**Tom Paulus:** Subjektivně mám pocit, že v angličtině to funguje líp. Když to máte v češtině, model si to často vnitřně překládá. Složité prompty pro automatizace dělám v angličtině. Ale pro běžnou práci je čeština v pohodě.

## Optimalizace promptů

**Tom Paulus:** Často používám **Anthropic Workbench** nebo **OpenAI Optimizer**.
Ukázka: Mám asistenta v Claude, kterému řeknu: „Potřebuji asistenta, který mi pomůže definovat role mých promptů na základě chatů, které mu poskytnu.“
On si sáhne do mého „Prompt Engineering“ promptu a začne tvořit.

Můžete vzít svůj prompt a vložit ho do **OpenAI Platform -> Optimizer**. Pošlete mu jakýkoliv prompt a ono ho upraví pro GPT-4/5 tak, aby s ním model lépe pracoval. Často přidá sekce, zlepší strukturu, přidá konkrétní roli. To je pro mě většinou poslední krok před tím, než prompt nasadím do ostrého provozu.

## Další techniky

*   **Few-shot prompting:** Dejte AI ukázky výstupu (jak to má a nemá vypadat).
*   **Prompt Chaining:** Rozdělte práci na kroky. Nesnažte se udělat vše v jednom promptu. Například: 1. Stáhni data, 2. Analyzuj data, 3. Vytvoř identitu. Kdybych to udělal najednou, AI na něco zapomene nebo začne halucinovat.
*   **Reverzní inženýrství:** Mám prompt (od Filipa Dřímalky), kterému dám text/výstup a on mi napíše prompt, který by takový výstup vytvořil. Skvělé pro kopírování stylu, který se vám líbí.
*   **Panel expertů:** Prompt, který vytvoří virtuální diskuzi mezi experty na dané téma. Vy z té diskuze pak dostanete závěry.

## Co když to nefunguje?

**Tom Paulus:**
1.  Nahrajte prompt a špatný výstup zpět do AI a zeptejte se: „Co jsi udělal špatně? Jak upravit prompt?“
2.  Zeptejte se asistenta: „Jaké informace potřebuješ, abys produkoval lepší výsledky?“
3.  Buďte přímí. Nemusíte prosit a děkovat. Čím přímější jste, tím lepší výsledky (hlavně u složitých úloh).

**Dotaz z chatu:** Je normální, že mi GPT dá výsledek až druhý den?
**Tom Paulus:** Ne. Pokud AI řekne „ozvu se ti zítra“, tak se neozve nikdy. Je to bug nebo halucinace. AI pracuje teď. Pokud se to zasekne, začněte nový chat, upravte prompt nebo zmenšete kontext.

**Dotaz z chatu:** Jak donutit GPT nevymýšlet si u odborných témat?
**Tom Paulus:** Máme v instrukcích: „Pracuj jen s daty, která máš k dispozici, nevymýšlej si.“ Pomáhá chtít zdrojování (odkud informaci vzal). Ale jsou to statistické modely, z podstaty věci si budou vymýšlet. Nejlepší je mít vlastní vektorové databáze (RAG), kde AI hledá jen ve vašich datech.

**Dotaz z chatu:** Gemini vs. GPT vs. Claude?
**Tom Paulus:** Neexistuje odpověď, který model je nejlepší. Dělejte si „mini výběrka“. Zadejte stejný úkol všem a pokračujte s tím, kdo dal lepší výsledek. Gemini je skvělé v tom, že přímo v chatu umí dělat věci, které GPT dělá hůř (např. práce s Google Workspace), Claude má skvělý cit pro jazyk a kódování.

## Závěr

**Tom Paulus:** Snažím se mít věci přenositelné (v Markdownu), abych nebyl závislý na jednom nástroji. Je to trochu schizofrenie mít knowledge base na více místech, ale zatím to jinak nejde. Díky za pozornost.

**Aibility | Petra Květová Pšeničná:** Moc děkuju, Tome. Doufám, že jste si odnesli spoustu praktických rad. Zvu vás do AI EduStream, kde najdete záznamy a materiály. Zítra nás čeká webinář „Vaše největší AI příležitosti“ a v listopadu budeme řešit Cursor, etiku a další témata. Díky všem a mějte se hezky.

✅ Vyčištění dokončeno.