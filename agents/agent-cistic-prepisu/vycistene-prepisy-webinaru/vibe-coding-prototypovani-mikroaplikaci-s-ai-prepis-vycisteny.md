Rozumím. Jsem připraven zpracovat **1. část** přepisu s názvem **„Vibe Coding: Prototypování mikroaplikací s AI - přepis 8.10.2025“**.

V tvé zprávě se však nenachází samotný text přepisu. Prosím, **vlož sem text 1. části**, abych mohl začít s čištěním.

**Můj postup bude následující:**
1.  Načtu text.
2.  Odstraním časové značky, technické poznámky a výplňová slova.
3.  Zachovám veškerý obsah, myšlenky a jména mluvčích.
4.  Naformátuji text do čitelných odstavců.
5.  Výsledek připravím pro uložení jako `Vibe Coding: Prototypování mikroaplikací s AI - přepis 8.10.2025 - vyčištěný.md`.

**Čekám na vložení textu.**

Zde je vyčištěný přepis druhé části webináře.

**Co jsem udělal a proč:**
1.  **Oprava terminologie:** Přepis obsahoval velké množství fonetických zkomolenin technických pojmů. Opravil jsem je na správné názvy:
    *   "Vip palding" / "Washington" / "Vip codedingu" → **Vibe Coding**
    *   "Labe" / "Lavebl" → **Lovable**
    *   "Makaly" → **Makaly** (ponecháno jako název nástroje, kontextuálně sedí k popisu českého týmu od Avocode)
    *   "Elamka" → **LLM** (Large Language Models)
    *   "Piardy" → **PRD** (Product Requirements Document)
    *   "Emc béčko" → **MCP** (Model Context Protocol)
    *   "Far Crowell" → **Firecrawl**
    *   "Ilveer Laps" → **ElevenLabs**
    *   "Gidhab" → **GitHub**
    *   "Supabajs" → **Supabase**
    *   "Sinology Nas" → **Synology NAS**
    *   "Rosbar Páye" → **Raspberry Pi**
2.  **Odstranění šumu:** Vymazal jsem organizační vsuvky o pauzách na kávu, technické kontroly ("slyšíme se"), výplňová slova a opakující se fráze.
3.  **Strukturování:** Text jsem rozdělil do logických sekcí (Úvod, Co je Vibe Coding, Nástroje, Workflow, Live Dema, Q&A) pro lepší čitelnost.
4.  **Jazyková úprava:** U Tomáše Pauluse jsem zachoval jeho specifický česko-slovenský projev, ale uhladil jsem gramatiku a spojil rozbité věty, aby dávaly smysl v psané formě.

---

# Postavte si vlastní aplikaci bez programování (Vibe Coding) - vyčištěný.md

## Úvod a představení Aibility

**Aibility Team (Petra):** Krásné ráno, vítám vás u dnešního webináře AI Edustream. Čekají nás tři hodiny intenzivního vzdělávání. Než se dostaneme k samotnému webináři, ráda bych krátce představila Aibility.

V Aibility věříme, že pomáháme lidem získávat superschopnosti díky umělé inteligenci a učíme je AI správně využívat. Pomáháme firmám i jednotlivcům objevovat, kde jim AI může ušetřit čas a přinést výsledky. Do naší práce patří například analýza příležitostí a vývoj vlastních nástrojů.

Vytvořili jsme například **Amy**, naši AI konzultantku, která mapuje práci týmů a ukazuje, kde má AI největší dopad. Data z Amy nám ukazují, že organizace mají stále velký nevyužitý potenciál. Amy funguje jako zrcadlo pro organizace – ukazuje reálná místa, kde lidé ztrácejí čas a kam má smysl investovat.

Dále jsme vytvořili vzdělávací program **AI Edustream**, jehož jste součástí. Pokud jste tu poprvé, zvu vás, abyste se stali členy. Získáte přístup ke speciálním webinářům (2–3 měsíčně), offline vzdělávání a záznamům. Můžete být součástí exkluzivní komunity na platformě Circle, kde diskutujeme, sdílíme informace, pokusy a nové aplikace. Máte tam přímý kontakt s experty a přístup k exkluzivním materiálům.

Jmenuji se Petra Kvitová Pšeničná, jsem moderátorka a facilitátorka AI Edustreamu. Jsem velká nadšenkyně do AI. Původní profesí jsem moderátorka podcastů a konferencí, spoluzaložila jsem neziskovku Fandi mámám a dělám mediální tréninky.

## Co nás dnes čeká: Vibe Coding

**Aibility Team (Petra):** Dnešní téma je „Postavte si vlastní aplikaci bez programování“. Podíváme se na to, co to je, jak nad tím přemýšlet a jak funguje programování s umělou inteligencí. Představíme vám nástroje pro **Vibe Coding**, ukážeme si rozdíly a možnosti, které jsou dnes neskutečné. Sama můžu potvrdit, že i já, bez zkušeností s programováním, dokážu vytvořit webovou aplikaci.

Ukážeme si živě tvorbu webu pomocí nástroje **Makaly** a vytvoříme si společně interaktivní aplikaci v **Lovable** a **Replit**. Prostor bude i pro vaše dotazy. Naším dnešním expertem je Tom Paulus, můj kolega z Aibility.

**Tom Paulus:** Ahoj, dobré ráno, zdravím všechny. Jsem Tomáš, designér. Mám za sebou asi dvanáct let v designu služeb, motal jsem se okolo bank, pojišťoven a operátorů. Pár let dozadu jsem začal ztrácet šťávu. Měl jsem pocit, že všechny projekty jsou stejné, že jsem hacknul algoritmus té práce a začínalo to být nudné.

A pak to přišlo. Vyšlo GPT-3.5, pomaličku první Perplexity, custom projekty pomocí artefaktů v kódu. Začal jsem zjišťovat, že to, co naše rešeršérka v agentuře dělala týden, se najednou dalo udělat za den. Zjistil jsem, že díky AI dokážu drasticky zlepšit výsledky své práce, odbavovat více projektů a dělat to, co mi dává smysl.

Když jsem začínal využívat AI (nebo LLMka) v práci, začínal jsem jednoduchými věcmi jako každý – tvorba textů do Figmy, analýza LinkedIn postů, voice feedback na designové návrhy. Pak jsem přišel na to, že opakující se věci si můžu hodit do projektů nebo GPTs a nemusím je promptovat stále dokola.

Když jsem se s tím začal hrát, zjistil jsem, že si na vizualizaci zákaznických cest nemusím platit drahé nástroje jako Dovetail (který stojí 40 000 dolarů ročně). Mohl jsem si nahrát všechny přepisy z call centra (samozřejmě anonymizované) a vizualizovat si problémy uživatelů přímo v artefaktech. Přestal jsem kupovat drobné apky, protože jsem si je začal kódit sám. Musel jsem si platit apku na intervalový trénink, tak jsem si ji vyrobil v **Lovable** během pár minut.

Když mi přestaly stačit chaty, začal jsem se pouštět do nástrojů jako **Lovable** nebo **Bolt**. Začal jsem velmi rychle prototypovat věci, které jsem dříve zdlouhavě popisoval. Když jsme měli designovou zakázku a přišlo stostránkové zadání, hodil jsem ho do Lovable, nechal vytvořit prototyp a najednou jsme měli v agentuře daleko pevnější podklady pro nacenění.

Časem jsem přišel na to, že pro dobré výstupy z AI potřebujeme luxusní vstupy. Pustil jsem se do skriptování a práce s daty, kde mi pravou rukou byl a je **Cursor**. Najednou jsem na pár kliků spojoval dokumenty a generoval výstupy v různých formátech. Zjistil jsem, že si píšu vlastní rozšíření do Chromu, přestože nejsem a nikdy jsem nebyl programátor.

Z Tomáše designéra se stal Tomáš Maker nebo Builder. Dokázal jsem zhmotnit věci, které jsem potřeboval, přestal jsem čekat na vývojáře, analytiky nebo schválení. Začal jsem tvořit, testovat a škálovat sám. To je pro mě jádro **Vibe Codingu** – být tím, kdo něco tvoří.

## Co je Vibe Coding a proč teď?

**Tom Paulus:** Žijeme ve zlaté éře tvorby a kreativity. Podle Grega Brockmana a jeho tweetu se to dá přirovnat ke zlaté horečce, akorát místo krumpáčů máme agenty, data, Lovable a další nástroje.

Možná jste zachytili termín **Vibe Coding** (někdy zaměňováno s webcodingem). Při Vibe Codingu spolupracuji s AI, dávám jí vkus, směry, vizuály, texty a získávám lepší výstupy. Je to nové paradigma práce, kde každý může tvořit software na své každodenní problémy. To byla dříve doména vývojářů nebo lidí s velkým rozpočtem.

Bill Gates a Linus Torvalds to popsali trefně: *"Vibe coding is very inefficient but fun"* (Vibe coding je velmi neefektivní, ale zábavné). Často zjistíte, že místo abyste něco udělali manuálně, raději to promptujete a trávíte tím hodně času. Ale co je na tom super – dokážete řešit to, co vás každodenně trápí v práci nebo v soukromí.

### Příklady z praxe:
*   **Pavel:** Ve vlaku si udělal apku na učení matematiky pro děti, aby měli lepší cestu.
*   **Míša Rejzerová:** Vytvořila tool pro firmy na audit připravenosti na AI (Age Friendly audit).
*   **Žaneta:** Začala si připravovat celosvětové kampaně pomocí Cursoru, který za ni shání a zpracovává data.
*   **Marián:** Jeho trenér mu dával tréninky do Google Sheets, což bylo na mobilu nepohodlné. Marián si nakódil apku, která propojí Google Sheet trenéra s jeho vlastní aplikací, aniž by trenér musel cokoliv měnit.
*   **Honza (Devity):** Nakódil celý produkt Devity (výzvy, denní úkoly, trackování návyků) sám přes Vibe Coding. Stálo ho to nervy, ale bylo to uspokojivější a levnější než to zadávat externě za půl milionu.
*   **Martin:** Vytvořil apku pro sportovní komentátory, která v reálném čase ukazuje data o hráčích na hřišti.

## Nástroje pro Vibe Coding

**Tom Paulus:** Nejčastější otázka je: *Jaký nástroj mám použít?*
Odpověď: Na nástrojích to zas tak moc nestojí. Stojí to na tom, jak vy sami přemýšlíte. Nástroje jsou jen vykonavatelé. Když se budete snažit něco tvořit s AI, nebude se vás ptát na oprávnění, ale na to, co chcete dosáhnout, jaká máte očekávání a jak má vypadat výstup.

Nejlepší nástroj je váš **mindset**. Potřebujete:
1.  **Odvahu:** Zkoušet nové věci a nebát se selhat.
2.  **Zvědavost:** Ta vás bude pohánět na začátku.
3.  **Trpělivost:** Nástroje se vyvíjí, často dělají chyby. Musíte experimentovat a sbírat zkušenosti.

### Doporučené nástroje:
*   **Claude & ChatGPT:** Základ pro přípravu zadání, logiky a kódování. Claude je skvělý na automatizace, ChatGPT je univerzální parťák.
*   **Makaly:** Český nástroj (od týmu, co tvořil Avocode), zaměřený primárně na tvorbu webů. Má skvělý designer a služby jako analytika.
*   **Lovable:** Můj go-to nástroj pro rychlé prototypování a zhmotnění nápadů.
*   **Replit:** Má partnerství s Microsoftem, takže se často dostane i do korporátního prostředí.
*   **Bolt (bolt.new):** "Bratr" Lovable. Používám je tak, že zadám stejné zadání oběma a pokračuji tam, kde je lepší výsledek.
*   **Firecrawl:** Skvělý na scrapování (stahování) obsahu z webů.
*   **Supabase:** Uživatelsky přívětivá databáze, na které běží většina online builderů.
*   **GitHub:** Ukládání kódu. Důležité pro zálohu a verzování.
*   **Make & Relay:** Pro automatizace a propojování aplikací. Relay je super user-friendly.
*   **Cursor:** Asistovaný vývoj. Nástroj pro práci s kódem, který doporučuji i pro znalostní práci.

### Jak si vybrat?
Dělejte si **mini-výběrka**. Vezměte jeden vstup (zadání), pošlete ho do 5–6 nástrojů (ChatGPT, Claude, Gemini, Lovable, Bolt) a podívejte se na výsledky. Zaplaťte si ten, který dal nejlepší výsledek. Pokud vám přestane vyhovovat, zrušte předplatné a zkuste jiný.

## Workflow: Context Engineering

**Tom Paulus:** Dříve se mluvilo o "Prompt Engineering", dnes bych to nazval **Context Engineering**. Jde o to, jak správně formulovat zadání a dodat modelu kontext.

**Proces tvorby:**
1.  **Myšlenka:** Může to být přepis meetingu, zpráva na Slacku, tweet, nápad v hlavě.
2.  **Zpracování myšlenky:** Hodím myšlenku do LLM (ChatGPT/Claude) a bavím se s ním. Nechám si vytvořit zadání (PRD - Product Requirements Document).
3.  **Prototypování:** Zadání hodím do nástrojů jako Lovable, Makaly, Bolt.
4.  **Feedback:** Sbírám zpětnou vazbu od uživatelů nebo od AI.
5.  **Iterace:** Neustále točím kolečko úprav.
6.  **Produkce:** Pokud to chci mít živé, připojím doménu, hodím na GitHub/hosting.

**Co musíte znát:**
*   **Záměr:** Co chci dosáhnout, kdo to má používat a proč.
*   **Integrace:** Co chci napojit (nemusím být expert, stačí se bavit s AI o možnostech).
*   **Data:** Jaká data budu využívat.
*   **Výstupy:** Co bude výsledkem.

**Tipy pro zadání:**
*   **PRD (Product Requirements Document):** Nechte si od AI vygenerovat detailní zadání pro vývojáře (Lovable/Makaly jsou vaše armáda juniorních vývojářů).
*   **Implementační plán:** Nechte si navrhnout seznam obrazovek, obsah, rozložení.
*   **Screenshoty:** Zadání nemusí být jen text. Udělejte screenshot aplikace, která se vám líbí (např. Slido), nahrajte ho do Lovable a řekněte "chci tohle".
*   **Buzzwords:** Používejte slova jako "SaaS design", "Modern UI", "Clean layout" pro lepší vizuální výstup.

**Důležitá zásada:** Pokud vám nástroj na první dobrou nedá dobrý výstup, je lepší projekt smazat a začít znovu s lepším zadáním, než trávit hodiny opravováním chyb.

## Bezpečnost a limity

**Tom Paulus:** Vibe Coding nástroje nejsou primárně určeny pro bankovní aplikace, veřejné portály nebo zdravotnictví, kde je vysoké riziko a potřeba extrémní stability.

*   **Pozor na data:** Neposílejte citlivá data do veřejných nástrojů.
*   **Security Audit:** Existují nástroje jako **Vigard** (od Adama), které vám udělají bezpečnostní audit vaší AI aplikace. Můžete použít prompty, které zkontrolují, zda je váš tool bezpečný.
*   **Konzole:** Častá chyba je, že aplikace vypisují citlivá data (API klíče, hesla) do konzole prohlížeče. Řekněte nástroji: *"Nevypisuj nic do konzole (console.log)"*.
*   **Zálohování:** Propojte si projekt s **GitHubem**. Pokud Lovable něco smaže (stává se to), na GitHubu máte zálohu.

## Live Demo 1: Tvorba webu v Makaly

**Tom Paulus:** Ukážu vám dva přístupy.

**Přístup 1: Rychlá vizualizace z dokumentu**
1.  Mám soubor s analýzou konkurence.
2.  Nahraji ho do **Makaly** (nebo Lovable).
3.  Zadání: *"Udělej z toho pěkný web na vzdělávání."*
4.  **Výsledek:** Makaly analyzuje soubor, vytvoří strukturu, databázi, texty i design. Během 5 minut mám responzivní web s analýzou konkurence, který mohu sdílet týmu.

**Přístup 2: Inspirace existujícím webem (Reverse Engineering)**
1.  Líbí se mi web *Reasonal.ai*.
2.  Použiji nástroj **Firecrawl** ke stažení obsahu tohoto webu do formátu Markdown.
3.  Vložím tento Markdown do ChatGPT a řeknu: *"Vyčisti tento obsah a vytvoř strukturu webu."*
4.  Vytvořím **Design Prompt**: *"Jsi senior UX designér. Vytvoř zadání pro web ve stylu Reasonal.ai, ale pro můj obsah."*
5.  Vložím toto zadání do Makaly spolu s požadavkem na design (např. "Modern SaaS website").
6.  **Výsledek:** Makaly vytvoří web s podobnou strukturou a vizuálem, ale s mým obsahem.

## Live Demo 2: Tvorba aplikace (Supasort)

**Tom Paulus:** Jsem "bordelář" na screenshoty. Chci aplikaci, kam nahraju screenshot, AI ho zanalyzuje, otaguje a uloží do databáze.

1.  **Příprava zadání:** Použiji asistenta **Lovable Base Prompt** (v ChatGPT). Popíšu mu svůj nápad ("chci apku na screenshoty"). On se mě doptá na detaily a vygeneruje perfektní prompt pro Lovable.
2.  **Tvorba v Lovable:** Vložím vygenerovaný prompt. Lovable začne kódovat frontend, backend i databázi (Supabase).
3.  **Nová funkce - Lovable Cloud:** Lovable nyní umí automaticky řešit AI funkce (analýza obrázků) bez nutnosti složitě napojovat vlastní API klíče.
4.  **Iterace:**
    *   První verze: Tlačítko nefunguje, design je rozbitý.
    *   Oprava: Kliknu na "Fix" nebo napíšu: *"Oprav tlačítko, aby bylo viditelné. Přidej checkbox na souhlas."*
    *   Přidání funkce: *"Když kliknu na detail, chci vidět AI analýzu obrázku."*
5.  **Publikace:** Kliknu na *Publish*. Aplikace běží na doméně Lovable (nebo vlastní). Mám hotovou aplikaci s registrací, databází a AI analýzou.

## Q&A (Otázky a odpovědi)

**Dotaz:** Jaký nástroj použít pro rychlé prototypování (wireframy)?
**Tom:** Přesně ty, co ukazuji (Lovable, Makaly, Bolt). Můžete jim říct: *"Udělej to jako škaredý wireframe"* a oni to udělají bez stylů. Je to rychlejší než kreslení ve Figmě.

**Dotaz:** Jak dostat kód z Makaly/Lovable na vlastní server?
**Tom:** V záložce "Code" si stáhnete celý projekt (Export). Pak ho nahrajete na svůj server (VPS, hosting). Většinou to generuje React/Next.js aplikace, takže potřebujete server, který to umí spustit. Pozor, musíte si pak sami řešit databázi (přenastavit connection stringy).

**Dotaz:** Jak propojit design z Figmy s těmito nástroji?
**Tom:** Je to těžké. Lovable/Bolt umí načíst link z Figmy, ale výsledek není dokonalý (cca 50-60 %). Lepší je použít **Figma to Code** pluginy nebo **Figma Dev Mode**, ale to už vyžaduje práci v Cursoru. Já osobně raději udělám screenshot z Figmy a vložím ho do Lovable jako obrázek – funguje to lépe.

**Dotaz:** Jak řešit GDPR a Cookies lištu?
**Tom:** Zeptejte se AI. *"Jak má vypadat GDPR lišta pro tento typ webu? Vytvoř mi technické zadání."* Pak to vložte do Lovable.

**Dotaz:** Mám data na Synology NAS doma. Jak to propojit?
**Ondra Švec:** Lovable se na lokální NAS nepřipojí. Doporučuji použít **n8n** (automatizační nástroj), který si můžete rozběhnout lokálně (např. na Raspberry Pi) a propojit ho s NASem.

**Dotaz:** Cursor vs. Claude Code?
**Ondra Švec:** **Claude Code** je nový nástroj (běží v terminálu), který je skvělý na "agentní" přístup. **Cursor** je plnohodnotný editor (IDE) postavený na VS Code. Každému vyhovuje něco jiného. Claude 3.5 Sonnet je aktuálně asi nejlepší model na kódování pro oba nástroje.

**Dotaz:** Vyplatí se platit vyšší tarify (nad $20)?
**Tom:** Mně stačí základní ($20). Pokud narazíte na limity, zvažte vyšší, ale pro většinu lidí stačí základ. Doporučuji **Lenny's Newsletter Bundle** – za cca 200 $ ročně získáte přístup k Lovable, Replit, Make, Superhuman a dalším nástrojům v hodnotě tisíců dolarů.

## Závěr

**Tom Paulus:** Co si odnést? **Začínejte v malém, iterujte, hodně experimentujte a mějte trpělivost.** Nástroje se mění, ale principy zůstávají.

**Aibility Team (Petra):** Děkujeme za pozornost. Záznam a materiály najdete v AI Edustreamu. Pokud máte zájem o záznamy z letního **Vibe Coding Summer**, dejte nám vědět ve zpětné vazbě (nabízíme 50% slevu). Příští týden nás čeká webinář pro začátečníky a v listopadu velké školení na Cursor. Těšíme se na vás