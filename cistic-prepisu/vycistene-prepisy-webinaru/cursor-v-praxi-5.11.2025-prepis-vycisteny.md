Tady je vyčištěný přepis webináře.

**Co jsem udělal:**
1.  **Odstranění technického šumu:** Vymazal jsem časové značky, systémové hlášky ("Audio shared by...") a opakující se hlavičky jmen.
2.  **Jazyková korektura:** Opravil jsem fonetické přepisy technických termínů (např. "Marga/Markan" $\rightarrow$ Markdown, "Gpp/Chedgii pití" $\rightarrow$ GPT/ChatGPT, "Notebook Allen" $\rightarrow$ NotebookLM, "Envídi" $\rightarrow$ Nvidia, "Vinsurf" $\rightarrow$ Windsurf, "Emcp" $\rightarrow$ MCP).
3.  **Úprava plynulosti:** Odstranil jsem nadměrné výplňové slova ("vlastně", "jakoby", "prostě", "ehm"), spojil roztrhané věty a rozdělil text do logických odstavců.
4.  **Zachování jazyků:** Ponechal jsem slovenštinu u Toma a češtinu u Petry a Martina, aby zůstala zachována autenticita záznamu.
5.  **Strukturování:** Text jsem rozdělil nadpisy podle témat (Úvod, Co je Cursor, Ukázky z praxe, Nastavení, Q&A).

Níže naleznete obsah souboru.

***

# Cursor v praxi: Od dokumentů k mini-aplikacím bez programování - přepis - vyčištěný.md

## Úvod a představení

**Petra Květová Pšeničná:** Krásné ráno. Já vás vítám u dnešního webináře AI EduStream. Jsem moc ráda, že jste si udělali čas, že jste si doufám udělali i třeba kávu nebo čaj na to, abychom se společně dneska dovzdělali. Na úvod jste viděli video o tom, co my v Aibility děláme – snažíme se, aby lidé díky nám a díky umělé inteligenci získávali superschopnosti.

Vítám vás tedy v rámci AI EduStream. Vítám všechny, kteří už v AI EduStream jste, ale i vás všechny, kteří jste se k nám připojili dneska poprvé. Pokud budete mít jakýkoliv dotaz, určitě se neváhejte zeptat.

Dovolte mi, abych se na úvod představila. Jmenuji se Petra Květová Pšeničná. Jsem moderátorka a facilitátorka AI EduStream. Kromě toho moderuji nejrůznější podcasty a akce. Také jsem spoluzakladatelka neziskovky Fandí mámám, kde pomáháme samoživitelkám, a lektoruji mediální trénink. Pokud se se mnou budete chtít spojit, budu moc ráda.

Dnes je před námi webinář s názvem **Cursor v praxi: Od dokumentů k mini-aplikacím bez programování**. My už jsme v rámci našich webinářů o Cursoru velmi často mluvili a vy jste se na něj často ptali. Dnes si ukážeme, jak Cursor ovládnout, protože je to jeden z našich nejoblíbenějších nástrojů. Kolegyně Verča dokonce psala, že už ho používá častěji než třeba ChatGPT nebo Claude. Uvidíme, jak na tom budeme všichni po dnešním webináři.

Co nás dnes čeká? Musíme si na úvod říct, že Cursor je nástroj pro znalostní práci. Skutečně to není nástroj, který musí používat jenom programátoři. My vám dnes ukážeme, na co se dá využít a jak s tím pracovat. Ukážeme si, jak zapojit Cursor do práce, jak si ho nastavit a jak aktivovat agenta. Dozvíte se o klíčových funkcích, o tom, jak vypadá celé rozhraní a jak se přistupuje k souborům. Bude to velmi praktické. Ukážeme reálné příklady, tedy to, jak my používáme Cursor a na co konkrétně se dá využít.

Protože máme rádi, když dostanete nějaký materiál, který můžete používat i ve svém volném čase při zkoušení hluboké práce s AI, máme pro vás připravené konkrétní návody a přehledy funkcí. Tomáš, dnešní lektor, připravil velmi přehledný materiál, ke kterému se určitě dostaneme a budeme vám ho sdílet.

Základní informace pro všechny: Záznam z dnešního webináře budete mít k dispozici. Budete mít celé video, přepis i prezentaci. Bude to k dispozici i ve formě podcastu, takže si webinář můžete pustit třeba v autě, tak jako to děláme u všech webinářů na AI EduStream. Nemusíte se bát, že byste o něco přišli.

Pokládejte otázky. Budeme velmi rádi, když se budete ptát, protože chceme, aby to pro vás bylo co nejpřínosnější. Praktické otázky můžete pokládat jak do chatu, tak do Q&A. Q&A je lepší, protože nám tam nezapadne žádný dotaz a vidíme, jestli už jsme na něj reagovali. Najdete to na liště v Zoomu. Do chatu vám budeme posílat i nejrůznější odkazy k tomu, o čem zrovna mluvíme.

Kdo nás provede dnešním webinářem? Jsou tady mí dva skvělí kolegové, Tom Paulus a Martin Imrich. Oba jsou mí kolegové z Aibility. Můžete se s nimi spojit na LinkedInu, ať se nám ta komunita rozrůstá. První si vezme slovo Tom. Tome, vítám tě, i Martina. Hezké dopoledne a předávám ti slovo.

## Co je Cursor a proč ho používat

**Tom Paulus:** Dobré ráno, zdravím všetky. Ďakujem, Peťi. My sme vždy, keď sme niekde o Cursore v minulosti hovorili, začínali tým, že je to rozhranie pre vývojárov. Ale nebojte sa, ja som si povedal, že to skúsime inak. Ono je to hrozný strašiak, keď začnete prezentáciu o Cursore tým, že je to prostredie pre vývojárov. V skutočnosti je Cursor v podstate iba obyčajný textový editor, ktorý má dostupné AI pre prácu s textom, s dokumentmi a hlavne so súbormi na vašom disku.

Predstavujte si Cursor ako obyčajný obal všetkých AI modelov, ktoré bežne poznáte a používate – či už je to ChatGPT, Claude a spústa ďalších, ktoré viete v rámci Cursoru používať. To je obrovská výhoda Cursoru, že máte dostupné rôzne modely v jeden moment a tie modely sa prepínajú podľa úlohy, ktorú robíte. V princípe je to skutočne, nezávisle od toho, ako strašidelne to môže na prvý dojem pôsobiť, obyčajný textový editor, tak ako sme kedysi dávno na Windows používali Notepad. Tak si môžete predstaviť Cursor, ktorý má ale obrovské množstvo rôznych AI funkcií, ktoré nám znalostným pracovníkom dokážu extrémnym spôsobom zjednodušiť život.

Pre nás v Aibility je Cursor absolútny "game changer" pre znalostnú prácu. On síce vznikol ako nástroj pre programátorov, ktorý im má pomôcť zefektívniť programovanie, ale keď to stiahneme na našu znalostnú prácu, tak tie use-cases sú vlastne to programovanie, ktoré sa dá využívať, a pritom nemusíme byť vôbec programátori.

To, čo my bežne v Aibility s Cursorom robíme, sú rôzne prevody a transformácie dát. Vezmem jeden formát, zmením ho na iný formát. Vezmem tabuľku, spravím z toho iné súbory. Vezmem tabuľku, spravím z toho prezentáciu. Úplne bežne s tým analyzujeme obsah alebo ho tvoríme. Analyzujeme s ním marketingové reklamy, pomáha nám organizovať si našu internú Knowledge Base, čo je bežná súčasť znalostnej práce. Potrebujete mať nejakú hromadu kontextu, s ktorým často pracujete a ku ktorému často pristupujete. Pomáha nám vyhľadávať a pracovať s dokumentmi, ktoré máme v celej firme. Pomáha nám skriptovať automatizácie a vlastne ich programovať. Často tomu vlastne nemusíme vôbec rozumieť. Ja poviem Cursoru, čo po ňom chcem, a on to za nás urobí lokálne na našom počítači, na našich dátach, aby sme o tie veci neprišli. Zároveň dokáže využívať všetko, čo tie Mac-y alebo vaše počítače poskytujú – všetky terminály a rôzne programátorské veci, ktoré sú často zložité na pochopenie.

S Peťou sme sa dohodli, že vám urobíme malinkú anketu, nech vieme, či tu je niekto, kto s Cursorom už má alebo nemá skúsenosti.

**Petra Květová Pšeničná:** Aktuálně jsem nasdílela anketu. Dáváme zhruba minutku na odpovědi, abychom věděli, na koho zaměřit celý webinář. Zatím to vypadá, že je tady převaha lidí, kteří o Cursoru slyšeli, ale zatím nezkusili. Budeme věřit, že po dnešku se na to všichni vrhnou.

*...průběh hlasování...*

Ukončuji hlasování. Výsledky: 63 % lidí slyšelo o Cursoru, ale nezkusilo. 6 % aktivně používá, 26 % zatím jen krátce a 5 % slyší o Cursoru poprvé. Je to na tobě, Tome, abys jim ukázal, jak se do Cursoru zamilovat.

**Tom Paulus:** Je to tak. Ja Cursor používam prakticky častejšie než čokoľvek iné, než akéhokoľvek iného asistenta. Primárne preto, že Cursor je zložený z niekoľkých kociek. Tá prvá je, že je to naozaj textový editor, ktorý pracuje so súbormi na vašom počítači. Tá druhá je v pravej časti – klasické chatovacie okno, ktoré všetci poznáme z asistentov a AI nástrojov. Je to komunikačné rozhranie s tými LLM modelmi. Cursor ho využíva práve na to, aby si vzal výstupy z tých modelov a pracoval so súbormi na vašom počítači.

Obrovská výhoda Cursoru oproti iným nástrojom je tá, že nemusí používať AI (LLMko) na úplne všetky úlohy. Pretože keď vy poviete ChatGPT "spočítaj mi tento riadok alebo tento stĺpec tabuľky a daj mi nejaký výsledok", tak sa vám veľmi často stane, že ChatGPT po ceste niekde začne halucinovať, niečo vynechá alebo zmení výstup. V Cursore sa vám to s veľkou pravdepodobnosťou nestane, pretože on si naprogramuje na to programček, ktorý to sčíta normálne matematicky. A potom vám to vráti ako reálny výstup matematickej úlohy. To je veľký rozdiel oproti klasicky používaným nástrojom, ktoré používajú to LLMko prakticky na všetko. Cursor použije LLM na to, aby analyzoval váš dotaz, a potom sa rozhodne, či chce ďalej volať ChatGPT, Claude a tak ďalej, alebo či chce programovať.

To znižuje šancu, že bude halucinovať, a zároveň tú prácu extrémne zrýchľuje a pomáha nám prepoužívať to, čo bežne robíme. Pretože keď ja si napíšem: "Poprosím Cursor, aby mi napísal skript na sťahovanie webov a ukladal to do Markdown súborov," tak Cursor to raz napíše a potom vždy, keď budem chcieť ten obsah sťahovať, tak si zavolá nejaký svoj skript. Ja vlastne nemusím vôbec vedieť, ako ten skript funguje. Cursor si všetky chyby a celé fungovanie toho skriptu "handluje" sám. Robí to programovo, nie pomocou AI nástroja.

## Rozhraní Cursoru

**Tom Paulus:** Než sa pustíme do konkrétnych ukážok s Martinom, urobím vám veľmi rýchly "masterclass" z toho rozhrania. Keď si otvoríte Cursor prvýkrát, veľmi pravdepodobne uvidíte okno rozdelené na časti. V pravej časti vidíte nejaký chat (ak ho nevidíte, zapína sa ikonkou Cursoru vpravo hore). To sa volá "Agent" alebo "Composer". Je to normálne chatovacie okno, ako keby ste si otvorili ChatGPT.

Buď máte zvolený mód "Auto", to znamená, že Cursor si sám vyberie model, s ktorým pracuje, alebo máte zvolený nejaký konkrétny model. Napríklad Filip Dřímalka u nás má neustále zvoleného Sonnet. Ja si vyberám modely podľa toho, v akej fáze práce som. Keď teraz veľa programujem a potrebujem sa vymotať z nejakých chýb, vyberám si GPT-4o alebo Sonnet. Keď robím nejaké hlúpejšie úlohy, nechávam to na Cursor, ale veľká výhoda je, že si tie modely viem vybrať.

Vy môžete zo začiatku Cursor používať len tým, že sa začnete baviť s tým chatom a on si už tie súbory niekam uloží. Alebo je druhá možnosť – vytvoríte si nejakú zložku v sebe v počítači, kliknete na "Open Project", vyberiete si tú zložku a už pracujete v tej danej zložke. Cursor pristupuje k tým súborom, ktoré v tej danej zložke sú. On nebude pristupovať ku všetkým súborom vo vašom počítači, ak mu to explicitne nepoviete. Nemusíte sa toho báť. Na konci mám nejaké nastavenia, ako si zablokovať mazanie súborov, zablokovať niektoré zložky a podobne.

Keď si otvoríte nejaký projekt, rozhranie bude rozdelené na tri časti:
1.  **Ľavá časť:** Zoznam súborov vo vašej zložke. Cursor to volá "projekt", ale je to skutočne iba zložka, kde máte uložené súbory (fotky, tabuľky, Markdown súbory, prakticky čokoľvek). Je to zložka, do ktorej vám bude Cursor tvoriť výstupy a ku ktorej pristupuje. Viete tam pridávať nové súbory a zložky, rovnako ako vo Finderi na Macu.
2.  **Prostredná časť:** Zobrazenie obsahu súborov. Občas tam uvidíte kód, tabuľku, Markdown súbor alebo textový súbor. Je to to isté, ako keby ste si otvorili Word alebo čokoľvek iné. U mňa je to v majorite prípadov Markdown súbor (súbor formátovaný pomocou hviezdičiek a hashtagov).
3.  **Pravá časť:** Komunikačné rozhranie s Cursorom, do ktorého zadávate príkazy a odkazujete sa na zložky.

Teraz skočíme do demíčiek a ukážeme to prakticky.

**Petra Květová Pšeničná:** Zastavím vás, protože naskákalo moc dotazů k začátku používání. Vyžaduje Cursor instalaci, nebo existuje webová varianta? A existuje instalace pro Linux?

**Tom Paulus:** Áno, existuje webová varianta, ale podľa mňa funguje trochu inak než tá nainštalovaná. Tým, že je to na Mac, tak si myslím, že to bude aj na iné systémy. Ale je to otázka – vyžaduje inštaláciu? Pre mňa osobne, pokiaľ si Cursor nenainštalujem, tak strácam obrovskú časť jeho sily, pretože chcem, aby pracoval s mojimi súbormi a pristupoval k tomu obrovskému kontextu, ktorý u seba mám.

**Petra Květová Pšeničná:** Další dotaz: Mohli bychom ukázat setup, co musí být nastavené, aby měl Cursor přístup do Clauda a tak dále? Je to součástí předplatného?

**Tom Paulus:** Áno, súčasťou v tom Cursore sú AI modely. Keď sa pozriem do svojho Cursoru, kde mám predplatné to klasické za 20 dolárov, tak tam vidím práve model `cursor-small`, `claude-3.5-sonnet`, `gpt-4o`, `haiku` a ďalšie. Takže je to v predplatnom. Sú samozrejme obmedzené objemom tokenov, ktoré viete využiť. Každý model má iný objem, pretože sú inak drahé. Ale sú súčasťou. Nemusíte mať nastavené nič špeciálne, aby Cursor mal prístup ku Claudeovi, pretože je to súčasť predplatného. Potom samozrejme, ak chcem programovať aplikáciu, ktorá bude mať prístup do nejakých AI nástrojov, tak tam už využívam API kľúče.

**Petra Květová Pšeničná:** Je možné, aby Cursor viděl i na Google Disk, nejen lokálně?

**Tom Paulus:** Samozrejme. Viem, že tí, čo majú Google Disk, ho majú vlastne pridaný vo svojom počítači ako cloudový disk. Ja tak mám urobený iCloud – všetky moje projekty Cursorové mám v iCloude a k nim mi pristupuje Cursor. To isté je pri Drive alebo Dropboxe. Vy ste schopní si Dropbox alebo Drive aplikáciu nainštalovať a mať to priamo v počítači ako súborový systém. Potom k tomu Cursor bez problémov pristupuje, pretože k tomu pristupuje ako k lokálnemu disku.

## Ukázky z praxe (Use Cases)

**Martin Imrich:** Super. Mne sa tam páčila ešte jedna otázka na adopciu vo veľkých firmách a obava, že to pristupuje k súborom. Všetci programátori v Nvidii používajú Cursor pre svoju prácu – je ich 40 tisíc. Spústa firiem v Brne i Prahe používa Cursor ako asistenta pri vývoji. Ale my tu dnes máme webinár pre znalostnú prácu. My to používame trochu inak.

Máme pre vás niekoľko ukážok. Mám tu projekt, kde som si pripravil pár scenárov. Vľavo mám súbory, v strede hlavné okno a vpravo chat. Začneme jednoduchšími scenármi.

### 1. Převod formátů (CSV do Markdown)

**Martin Imrich:** Prvý jednoduchý scenár je prevod formátu. Tým, že Cursor pristupuje k lokálnym súborom, často riešime rôzne prevody. Nedávno sme riešili prevod videa so zlým kodekom, aby fungovalo v Zoomu. Cursor použil rôzne knižnice a previedol to.

Tu mám prípad, kedy robíme analýzy vo firmách. Výstup z analýzy často padá v CSV formáte (klasická tabuľka). Keď s tým chcem pracovať a ukázat výstupy zákazníkovi, chcem to dať napríklad do NotebookLM, ktorý ale umožňuje nahrávat iba Markdown, PDF nebo text, ale nie CSV.

Takže v chatu napíšu jednoduchý prompt:
> "Převeď tento soubor [přetáhnu soubor do chatu] do Markdown formátu, ať je možné ho nahrát do NotebookLM."

Mám tu režim **Agent**, který to promyslí, hledá věci a rovnou je vykonává. Nechám režim **Auto**, aby si Cursor vybral model. Cursor teď plánuje, čte soubor a velká výhoda je, že si vytváří skripty. Když nemá nainstalovanou knihovnu pro otevírání Excelu, doinstaluje si ji.

Vidím, že mi tvoří skript v Pythonu pro převod CSV do Markdownu. Kdybych měl těch souborů tisíc, tak si jednou vytvořím skript a pak to dělám opakovaně. Vidím, že mi vytvořil Markdown soubor. Můžu se na něj podívat – je to formát vhodný pro AI nástroje.

Potom můžu vzít ten skript a říct mu:
> "Použij stejný skript a převeď tento další soubor také."

On projde skript, případně ho upraví, pokud je druhý soubor v jiném formátu, a funguje agentsky.

### 2. Čištění a transformace dat

**Martin Imrich:** Druhý scénář je čištění dat. Exportujeme účastníky z našich akcí a dáváme je do databáze. Export ze Circle vypadá tak, že je tam spousta sloupců, které mě nezajímají. Potřebuji jen ID události, jméno a email.

Napsal jsem mu:
> "Použij ten skript a převeď mi tenhle soubor do podoby vhodné pro import do mé Supabase."

On to prošel, použil skript a vyšel z toho soubor, kde mám jen Event ID, lidi a email. Takhle jednoduše dělám převody formátů, transformace a čištění. Zvládá i tvorbu Excelů.

### 3. Web Scraping a stahování dokumentace

**Tom Paulus:** Jedna z vecí, ktoré ja často robím, je scrapovanie alebo sťahovanie informácií z rôznych webov. Prečo? Pretože na webe je všetka "knowledge" sveta a ja by som ju rád používal pri mojej práci. Môžem sa spoľahnúť na to, že poviem ChatGPT "prejdi túto stránku a vytiahni informácie", ale pre mňa je to často nespoľahlivé.

Pri príprave na minulý webinár o pokročilom promptovaní som chcel získať "Best Practices" od OpenAI a od Anthropicu. Manuálne som si vykopíroval zoznam odkazov, kde je relevantná knowledge o promptovaní Clauda a ChatGPT. Mám súbor `claude_links` so 14 linkami.

Povedal som Cursoru:
> "Potrebujem, aby si stiahol kompletný obsah stránok z odkazov, ktoré máš v súbore claude_links. Vytvor zložku Claude, stiahni všetkých 14 stránok a ulož ich ako individuálne Markdown súbory."

Cursor si spravil "to-do" list, vytvoril si skript, prechádzal jednotlivé stránky a sťahoval ich do Markdownu.

**Martin Imrich:** Tome, mohl bys říct, co to je Markdown?

**Tom Paulus:** Markdown formát je formát textových súborov, ktorý je nejakým spôsobom formátovaný, ako keď v Google Docs alebo vo Worde označíte text a kliknete, že to je "Nadpis 1". To isté robíte v Markdown formáte tým, že dáte napríklad `# Nadpis 1` alebo `## Nadpis 2`. Je to len druh súboru (prípona `.md`). Často sa používa pri práci s AI nástrojmi, pretože sa dobre číta a je dobre štruktúrovaný. Keď sa nechcem pozerať na hviezdičky a hashtagy, som schopný si to zobraziť pekne formátované (skratka `Command + Shift + V`).

Späť k use-case. Stiahlo mi to všetky zdrojáky ku Claudeovi aj OpenAI. Potom som v tom istom chate povedal Cursoru:
> "Potrebujem, aby si porovnal best practices pre promptovanie zo zložky Claude a zo zložky ChatGPT. Prejdi tie súbory, vyznač rozdiely a napíš mi návod, ako to používať v praxi."

Pripravil mi podrobný návod pre mojich študentov. Cursor pristupoval k mojim zložkám, analyzoval súbory a vytvoril krásny návod. Keby som to robil v ChatGPT, musel by som to robiť postupne po jednej stránke. Cursor, keď je kontext veľký, prechádza súbory jeden po druhom, analyzuje ich, ukladá si obsah do pamäte a potom to kombinuje.

Ďalší príklad: Existuje stránka `shapeof.ai`, kde je popísané, ako vytvárať stránky využívajúce AI. Nechal som si od Cursoru stiahnuť kompletne celú stránku, analyzovať obsah a vytvoriť Markdown návody. Hneď som to nahral na GitHub a všetci kolegovia to majú k dispozícii.

**Petra Květová Pšeničná:** Petra se ptá: Když se vytvoří nový soubor (převedený formát), uvidí ho i na svém disku, nebo jen v Cursoru?

**Tom Paulus:** Samozrejme na svojom disku. O to ide. Cursor pracuje s reálnymi súbormi. Vy mu môžete povedať "nič nevytváraj, iba odpovedaj do chatu", ale väčšinou si to chcete ukladať. Vo východzej pozícii všetko ukladá na disk.

**Petra Květová Pšeničná:** Je možné Cursor použít i na weby, na které máme login? Například stáhnout PDFka nebo přepsat video?

**Tom Paulus:** Veľmi dlhú dobu to nebolo možné. Ale pár dní dozadu som si sadol ku Cursoru a povedal som mu:
> "Potrebujem, aby si šiel na tento web. Tu je login. Na stránke XYZ nájdeš reporty. Potrebujem, aby si naklikal reporty za túto dobu a stiahol ich."

Cursor to zvládol. Napísal si krásny skript, otvoril si sám prehliadač, naklikal to, zistil kontext a stiahol reporty. Je to skôr o tom, či to nebude blokovať ten web. Osobne by som to nepúšťal na Facebook alebo Business Manager, aby vám nezablokovali účet, ale na iných bežných weboch by som sa toho nebál.

**Petra Květová Pšeničná:** Tomáš se ptá: Když má PDF soubory s grafikou, je nutné to vždy převést do Markdownu?

**Tom Paulus:** PDF súbory sú väčšinou len nejaký obal nad ďalším obsahom. Do Markdownu obrázky nedostanete (len ako odkaz). PDFka nie sú moc príjemné formáty pre LLMká, pretože si ich často musia prekladať. Ja to robím, pretože sa mi s tým lepšie pracuje.

**Petra Květová Pšeničná:** Vedeš si nějakou databázi, kam si Cursor sahá při každé iteraci?

**Tom Paulus:** Myslím si, že každý v Aibility má jednu zložku "Knowledge Base" (alebo "bordel zložku"), v ktorej má úplne všetko, čo robí s Cursorom. Vy ste schopní si kľudne tú zložku tvoriť z desaťtisícov súborov a povedať mu: "Nájdi mi tu ten projekt, urob toto." Ja si v tom držím trochu poriadok, ale ten poriadok mi môže udržiavať Cursor. Vy ste schopní povedať Cursoru: "Analyzuj obsah zložky X, povedz mi, čo sa v nej nachádza, navrhni novú štruktúru a presuň tie súbory."

### 4. Analýza dat a kampaní

**Tom Paulus:** Po 12 rokoch v digitále som potreboval nejakú zábavu offline, tak som začal spolupracovať s Metagym (svet fitka). Cursor mi pomohol analyzovať reklamnú kampaň. Stiahol som si zoznam všetkých predplatných, ktoré si ľudia kúpili za nejaké obdobie.

Povedal som Cursoru:
> "Toto je záznam predplatných. Od 2. 10. sme spustili novú reklamnú kampaň. Urob analýzu dopadu tejto kampane na predaje v Příbrami a Chodove. Vytvor nový Markdown soubor s názvem Kampaň analýza."

Cursor si načítal obsah súboru (má 100 000 riadkov), vytvoril si Python skript, aby ten súbor mohol prečítať efektívnejšie, a začal robiť analýzu. Hľadá všetko, kde je napísaná Příbram, vytvoril si porovnávacie premenné (pred spustením vs. po spustení kampane).

Keby som to robil v ChatGPT, je väčšia šanca, že začne halucinovať. Tu vidím, že za chvíľku mám krásne zhrnutú analýzu reklamy. Môžem to zobrať a zdieľať s tímom.

### 5. Tvorba obsahu a prezentací

**Martin Imrich:** Ja som robil analýzu našich analýz. Chystali sme webinár o tom, aké sú výsledky z analýz, ktoré robíme u klientov.

V prvom kroku som mu povedal:
> "Načítaj si našu Knowledge Base, aby si vedel, čo je Aibility a náš framework."

Potom som mu povedal, že chystáme webinár a potrebujem popis a štatistiky. Vďaka Cursoru som urobil celý skript na webinár. Na základe 312 analýz mi vytiahol, koľko ľudí je na akej úrovni používania AI, aké tam boli časové úspory a aké sú problémové oblasti.

K tvorbe prezentácií používam **Gamma**. Povedal som Cursoru:
> "Priprav mi jeden súbor, ktorý bude slúžiť ako text pre tvorbu prezentácie v Gamma. Chcem málo slidů. Vychádzaj z tých dát."

Cursor mi vytvoril text a spojovníky (oddeľovače pre slidy). Potom som ten text vložil do Gammy a ona mi vygenerovala prezentáciu.

**Petra Květová Pšeničná:** Zdeněk se ptá na doporučení rozšíření pro Markdown.

**Martin Imrich:** Je to **Markdown Preview Enhanced**. Doporučujem.

### 6. Mini-aplikace

**Tom Paulus:** Sľúbili sme aj mini-aplikácie. Vy si môžete nechať robiť veci programovo – buď hardcore coding celých aplikácií, alebo kľudne mini-aplikácie.

Ja som si nakódil mini-apku na skladanie promptov. Používam štruktúru: Hlavný produkt + Tone of Voice + Mód. Nechcelo sa mi to manuálne kopírovať. Povedal som Cursoru:
> "Chceme vytvoriť jednoduchú aplikáciu, ktorá načíta obsah zo zložky System. Potrebujem si vybrať prompt Core, Mód a Tón a vytvoriť finálnu kombináciu."

Cursor si zapol mód **Plan**, vytvoril si plán a začal programovať. Vytvoril jednoduchú webovú aplikáciu, ktorá beží lokálne. Ja si tam naklikám kombinácie a skopírujem výsledný prompt. Trvalo to asi minútu.

Tiež som si napísal vlastné rozšírenie do Chrome, ktoré mi stiahne aktuálnu stránku do Markdownu. Povedal som Cursoru: "Chcem rozšírenie do Chrome, ktoré aktuálne otvorenú stránku stiahne ako Markdown." Urobil to asi za 8 minút.

## Nastavení a tipy

**Tom Paulus:** Dôležité nastavenia (Settings):
1.  **Auto-Run / Run Terminal Command:** Cursor sa vás pri každom príkaze pýta na povolenie. Odporúčam zaškrtnúť "Run always", inak sa zbláznite z odklikávania.
2.  **File Deletion Protection:** Ochrana proti tomu, aby vám Cursor mazal súbory bez opýtania.
3.  **Dotfile Protection:** Nebude mazať skryté súbory (začínajúce bodkou).
4.  **External File Protection:** Cursor nesmie mazať alebo modifikovať súbory, ktoré sú v inom priečinku, než v ktorom pracujete (váš Workspace).

Pripravil som pre vás materiál – 15 kapitol, taká malá "biblia Cursoru". Máte tam všetko od základů, ako otvoriť súbory, formáty, best practices, tipy a triky.

**Martin Imrich:** Ešte k **MCP (Model Context Protocol)**. Je to protokol, ako si AI nástroje "rozprávajú" s inými službami. Mám napojený Cursor na náš Notion. Povedal som mu:
> "Pozri sa na štruktúru nášho Notionu, navrhni lepšiu štruktúru podľa metodiky GitLab Handbook a ulož to ako Markdown."

Vďaka MCP prešiel náš Notion a navrhol zmeny. Nastavuje sa to v *Settings -> Features -> MCP*.

## Q&A (Otázky a odpovědi)

**Otázka:** Proč jsi, Tome, dělal tu aplikaci v Laravelu a ne v Cursoru?
**Tom Paulus:** Pretože sa to oveľa horšie zdieľa. Laravel alebo Replit má tlačidlo "Publish". Keď to robím v Cursore, mám to u seba. Potrebujem to zavesiť na nejaký hosting.

**Otázka:** Stačí free verze?
**Tom Paulus:** Cursor nemá free verziu, má iba trial verziu na 14 dní (pozn. v prepise zaznelo 7 dní, ale štandardne býva 14, Tom hovorí 7). Je plnohodnotná, ale po uplynutí si musíte buď zaplatiť, alebo vytvoriť nový účet.

**Otázka:** Když může do mých externích dat (Google Disk), proč musím mít instalovanou verzi?
**Tom Paulus:** Pretože Cursor pracuje s reálnymi súbormi uloženými na disku. Aj k Google súborom pristupuje tak, ako keby ste ich mali uložené u seba (cez synchronizáciu). Webová verzia k lokálnym súborom pristupovať nevie.

**Otázka:** Rozdíl Cursor vs. VS Code vs. Windsurf?
**Martin Imrich:** VS Code + Copilot je alternatíva. Windsurf je tiež alternatíva. Je to o preferencii. My používame Cursor, pretože nám vyhovuje tá nadstavba.

**Otázka:** Dá se použít GitHub Copilot s editorem obdobně jako Cursor?
**Tom Paulus:** Dá, úplne rovnako. Je to len o kreativite.

**Otázka:** Co říkáte na nový model přímo od Cursoru (Cursor-small/Composer)?
**Tom Paulus:** Neskúšal som, vyšlo to asi 3-4 dni dozadu.
**Martin Imrich:** Tam je nově rozdělení pohledu Editor a Agent. Zatiaľ používam Editor, ale Agenti budú do budúcna veľmi zaujímaví (môžu bežať paralelne).

**Otázka:** Vzdálený přístup (Cursor na PC, ovládání z telefonu)?
**Tom Paulus:** Asi cez klasický vzdialený prístup k počítaču (TeamViewer a pod.).

## Závěr

**Petra Květová Pšeničná:** Je ještě něco zásadního, co by mělo zaznít?

**Tom Paulus:** Za mňa osobne: Experimentovanie. Začnite hneď a napíšte do Cursoru to isté, čo by ste napísali do ChatGPT. Uvidíte, čo vám to vypľuje. Pre mňa je to nástroj, ktorý mi extrémne zmenil prácu. Nepotrebujem si platiť nástroje na skriptovanie, mám Cursor.

**Martin Imrich:** Či si platiť GPT, Claude alebo Cursor? My používame všetko. GPT a Claude sú skvelé na brainstorming a majú projekty. Cursor je na prácu s lokálnymi súbormi. Je to o experimentovaní a hľadaní, čo zrovna potrebujem.

**Tom Paulus:** Ešte by som reagoval na Martina s tým návratom do lokálu. Podľa mňa to dáva extrémny zmysel. Kontext je kráľ. My sa všetci nenápadne zatvárame do "vendor lock-in" (závislosti na dodávateľovi) v momente, keď používame len ChatGPT alebo len Clauda. Čím dlhšie s nami AI nástroje budú, tým bude ten kontext podstatnejší. Pokiaľ budete mať svoj životný kontext iba v jednom nástroji, bude sa vám ťažko odchádzať. Vy chcete mať ten kontext u seba – lokálne, na Google Disku, v iCloude – ale aby to boli VAŠE súbory. To je vaša dlhodobá pamäť.

**Petra Květová Pšeničná:** Myslím si, že to je moc hezká tečka. Moc děkuju Tomovi i Martinovi. Vídáme se pravidelně na AI EduStream, kde vás rádi uvidíme. Máte tam k dispozici prémiové webináře, propojení s komunitou a experty. Děkuji za pozornost a těším se příště.

✅ Vyčištění dokončeno.