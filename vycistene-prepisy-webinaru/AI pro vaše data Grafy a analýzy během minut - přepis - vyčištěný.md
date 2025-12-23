Tady je vyčištěný přepis webináře.

**Co jsem udělal:**
1.  **Odstranění technického šumu:** Vymazal jsem časové značky, instrukce k nahrávání, technické kontroly zvuku a opakující se výzvy k psaní do chatu.
2.  **Oprava terminologie:** Přepis obsahoval mnoho fonetických zkomolenin (např. „Gpp“ → ChatGPT, „Džeminaj“ → Gemini, „Qui“ → Q&A, „Lavebem“ → Webflow, „Dia Brocer“ → Browse AI). Tyto názvy jsem opravil do správné podoby.
3.  **Jazyková korekce:** Odstranil jsem výplňová slova („eh“, „jakoby“, „vlastně“), spojil rozsekané věty a upravil slovosled pro lepší čitelnost, přičemž jsem zachoval hovorový styl a osobnost mluvčích.
4.  **Strukturování:** Text jsem rozdělil do logických sekcí s nadpisy (Úvod, ChatGPT, Manus, Dotazy), aby byl text přehledný.

---

# AI pro vaše data: Grafy a analýzy během minut - přepis - vyčištěný.md

**Host:** Dominik Palla (Programátor, lektor, výzkumník v oblasti AI)
**Moderuje:** Petra Květová Pšeničná (Aibility)
**Datum:** 22. 10. 2025

---

## Úvod a představení

**Petra Květová Pšeničná:** Krásné dopoledne. Vítám vás u dnešního dalšího webináře AI & Edu Stream. V Aibility se snažíme, abychom všichni získávali superschopnosti díky umělé inteligenci, a právě proto je tu tento stream.

S některými z vás se už známe, ale pro nováčky se v krátkosti představím. Jmenuji se Petra Květová Pšeničná, jsem moderátorkou a facilitátorkou AI & Edu Streamu. V Aibility jsem zatím krátce, zhruba od září, ale věřím, že se budeme potkávat stále častěji. Zároveň jsem spoluzaložila organizaci Fandi mámám. Budu moc ráda, pokud se spojíme například v rámci naší komunity Circle, kde si můžeme vyměňovat zkušenosti.

Dnes nás čeká webinář na téma **AI pro vaše data: Grafy a analýzy během minut**. Podíváme se na to, jak proměnit data v jasné odpovědi, jak nechat umělou inteligenci vytvořit přehledné grafy během pár minut, jak odhalit slabá místa ve výsledcích a jak vytvořit datovou analýzu i bez technických znalostí.

Záznam z webináře, prezentaci a přepis najdete jako vždy v naší komunitě na Circle v sekci Záznamy a materiály. Můžete si nás poslechnout i jako podcast. Dotazy pište ideálně do sekce Q&A na liště Zoomu, aby nezapadly v chatu.

Dnešním hostem je inženýr Dominik Palla. Je to nájemný programátor, akademický lektor programování a výzkumník v oblasti AI působící na Fakultě informatiky a managementu Univerzity Hradec Králové. Dominiku, vítejte, předávám vám slovo.

**Dominik Palla:** Dobrý den, děkuji za úvod, Petro. Zdravím vás všechny. Půjdu rovnou k věci. Ještě než začneme, připravili jsme si krátký dotazník, který nám pomůže lépe identifikovat, s čím bojujete a jaké nástroje používáte.

**Petra Květová Pšeničná:** Dotazník jsem sdílela. Zajímá nás, jaké nástroje používáte (ChatGPT Plus, Gemini atd.) a jaká je vaše profese.

*(Probíhá hlasování)*

Koukám na výsledky. Dominiku, nejvíce lidí, 88 %, využívá ChatGPT Plus. Hodně je zastoupená i Perplexity a Claude. Co se týče profesí, máme tu pestrou škálu: provozní ředitel v investiční společnosti, software developer, ekonom, knihovník, lektor, muzikolog, marketing IT, programátor, HR, operations manager, školitel nebo projektový manažer.

## Část 1: Analýza dat s ChatGPT

**Dominik Palla:** Děkuji. Dnešní workshop je rozdělen do dvou částí. První bude zaměřena na nástroj ChatGPT, který je mezi vámi nejpoužívanější.

Mám tu připravenou tabulku, která ukazuje tržby fiktivního zeleninářství za rok 2025. Obsahuje 365 řádků s informacemi o počtu zákazníků, útratě a dalších parametrech. Samozřejmě si můžete představit jakákoliv jiná data, se kterými pracujete – například počet prodaných kusů s mnoha sloupci.

Tato tabulka je zjednodušená a ChatGPT nám na ni bohatě postačí. Soubor jednoduše přetáhnu do chatu a požádám ho o zpracování. Mohu chtít průměry nebo vytvoření grafů.

Zadám příkaz: *"Můžeš mi prosím vypracovat nějaké hezké grafy?"*

Píšu to obecně, abychom viděli, co nabídne, ale vy můžete specifikovat, že chcete sloupcový graf, koláčový graf nebo průměrnou útratu napříč měsíci.

### Jak ChatGPT zpracovává data
Vidíme, že probíhá "Analýza". Když na to klikneme, vidíme, že ChatGPT sestavuje Python kód. To je důležité – pokud nejste programátoři, nemusíte kód číst, ale je to signál, že data jsou zpracovávána matematicky správně. Kdyby se začal generovat obrázek (DALL-E), zpozorněl bych, protože to by znamenalo, že se snaží data "namalovat", což by bylo nepřesné. My chceme striktní syntézu dat.

Vznikly nám grafy – sloupcové i složitější. Můžete si je zvětšit nebo nechat změnit barvu. Dříve byl problém, že při změně barvy se graf vygeneroval znovu a vypadal jinak, dnes už je to lepší. Grafy si můžete stáhnout jako obrázek. Pokud je použijete v práci, můžete uvést, že byly zpracovány přes Python knihovnu (např. Matplotlib/Seaborn), což zní profesionálněji než "udělala to AI".

### Limity ChatGPT
Výhodou ChatGPT je rychlost. Nevýhodou je omezená kapacita. Pokud bych mu dal tabulku se 100 000 řádky, už to nebude tak snadné. Napíše si skript, ale ten může běžet příliš dlouho a spadne to. V horším případě načte jen polovinu tabulky a dojde ke zkreslení, což v práci nemůžeme riskovat.

Zkusíme další příkaz: *"Můžeš mi udělat graf průměrné útraty po měsících?"*

Kromě grafiky si můžeme nechat napsat i slovní hodnocení: *"Můžeš mi na základě toho grafu slovně zhodnotit, kde jsou trendy a špičky?"*

To se hodí do prezentací. Pokud by nás to zajímalo více technicky, museli bychom ho o to požádat, případně mu nahrát formulář s konkrétními otázkami, které zajímají našeho šéfa.

### Generování reportů a dokumentů
Můžeme si nechat vytvořit kompletní report ve Wordu: *"Udělej mi kompletní report ve slovně, dej to do .docx."*

ChatGPT je schopen vytvořit dokument, který si stáhnete. Pozor, odkaz na stažení funguje zhruba 10 minut, pak soubor ze serverů smažou kvůli úspoře místa.

Pokud byste chtěli report delší než 2–3 strany, narazíte na limity. ChatGPT se snaží šetřit výpočetní výkon. Dlouhý text vám najednou nevygeneruje, museli byste ho žádat po částech.

**Petra Květová Pšeničná:** Dominiku, skočím vám do toho. Když nechám vygenerovat tabulku, stává se mi, že není dokonalá. Je to tím, že zadávám příliš mnoho dat? Doporučujete to nechat zkontrolovat nebo vygenerovat znovu?

**Dominik Palla:** Záleží, v čem není dokonalá. Obecně říkám, že práce s ChatGPT je jako volání na operátora. Když debata nikam nevede, je lepší zavěsit a zavolat znovu – tedy založit nový chat. Dostanete nový kontext. Pokud se s ním hádáte a on generuje nesmysly, nový chat často pomůže. Můžete mu také chybu vytknout: *"Takhle tu tabulku nechci, chci ji barevně a názorně,"* nebo *"Tady jsi udělal faktickou chybu."*

Pokud po něm chcete 30 specifických průměrů a on jich dává jen 10, a i po urgenci dává jen 10 (třeba jiných), narážíte na limity modelu.

### Problém s pamětí (Context Window)
Když vedete dlouhou konverzaci (např. hodinu a půl) a neustále doplňujete požadavky, ChatGPT začne zapomínat. Pamatuje si přesně jen posledních cca 10 zpráv. Starší zprávy si na pozadí sumarizuje. Z hodinové konverzace se v jeho "paměti" stane jeden odstavec. Tím se ztrácejí detaily a instrukce ze začátku konverzace. Je potřeba ho hlídat.

### PowerPoint a prezentace v ChatGPT
ChatGPT umí nativně pracovat s PowerPointem (.pptx).
Zadám: *"Dej mi to prosím do prezentace."*

Opět si napíše skript. Ale pozor, grafika bude velmi omezená – prostě tam "hodí" text a obrázky. Nevypadá to dobře. Pokud po něm budete chtít roztáhnout prezentaci na 30 slidů, buď to odmítne, nebo dá na každý slide jednu větu.

Také nedokáže dobře pracovat s firemními šablonami. Když mu pošlete šablonu vaší instituce, nedokáže se jí držet.

### Halucinace u videa a audia
Velký pozor si dejte při analýze videa nebo audia. Pokud mu nahrajete video a chcete přepis nebo analýzu, často řekne: *"Jasně, analyzuji to, jsem na 10 %... 20 %..."* Nakonec napíše, že to má hotové, ale pošle vám něco, co si úplně vymyslel. Vnitřní stav s procenty neexistuje, je to halucinace. Pokud nevidíte reálný přepis nebo kód, nevěřte mu.

Co se povedlo, bylo předabování krátkého videa (10–15 minut), kdy jsme mu dali video a jinou zvukovou stopu. To zvládl.

Abych ale jen nekritizoval – ChatGPT ze všech nástrojů nejlépe "přemýšlí" a simuluje uvažování. Jeho čeština je výborná a výstupy dávají smysl, což se nedá srovnat s jinými modely.

## Dotazy k první části

**Petra Květová Pšeničná:** Viktor se ptá: *"Při analýze otevřených odpovědí z dotazníku jsem dostával jen základní analýzu. Detailnější nasliboval, ale pak zjistil, že nemá knihovny. Je to stále omezení?"*

**Dominik Palla:** Posouvá se to, ale pořád bych tomu nevěřil u velkých dat. Tlačí na úsporu tokenů. Vybere si pár vzorových odpovědí a zbytek ignoruje. Pro vážnou analýzu to není ideální. Ukážu vám na to lepší nástroj v druhé části.

**Petra Květová Pšeničná:** Vladimír se ptá: *"Dají se data zpracovat do pokročilejších grafů a odeslat do Canvy?"*

**Dominik Palla:** Do Canvy to dostanete jako obrázek. ChatGPT umí přes Python exportovat různé formáty, i vektorové, ale 3D zobrazení mu moc nejde. Co se týče přímého konektoru do Canvy v rámci ChatGPT, nezkoušel jsem to, protože integrace bývají často nedotažené. Většinou je lepší to udělat ručně v cílovém nástroji.

**Petra Květová Pšeničná:** Mě napadá opačný postup. Mám data a chci z nich udělat Excel. Jde to? A je jedno, jestli používám Google Sheets nebo Excel?

**Dominik Palla:** Formát (Google/Excel) je jedno, on to přečte jako text. Vytvoření tabulky zvládne, ale ChatGPT je spíše sumarizační nástroj (z hodně dat udělá málo). Pokud chcete z mála dat udělat hodně (např. ke každému řádku dohledat něco na internetu), narazíte. U 360 řádků to možná půjde, u 10 000 ne.

## Část 2: Manus – Autonomní agent

**Dominik Palla:** Nyní vám představím nástroj **Manus**. Není to klasický chatbot jako ChatGPT nebo Perplexity, ale tzv. **agent**.

V ChatGPT možná znáte mód "Work with Apps" (interakce se zástupcem), ale ten funguje špatně. Když po něm chcete najít hotel, kliká vedle, vrací se, trvá mu to dlouho a výsledek nestojí za to.

Manus je v tomto mnohem dál. Nemá limity jako ChatGPT (kromě kreditu). Má vlastní izolované prostředí s virtuálním počítačem a prohlížečem.

### Co Manus umí
Manus dokáže samostatně pracovat. Můžete mu zadat úkol a on na něm pracuje klidně dvě hodiny.
*   **Analýza dat:** Zvládne stejnou analýzu tržeb jako ChatGPT, ale důkladněji.
*   **Tvorba webu:** Nedávno po mně chtěla Univerzita Karlova web pro rozcestník k respirátorům. Neměl jsem čas, tak jsem poslal podklady Manusu. On vytvořil funkční web, napsal kód, otestoval ho a nasadil. Já jen změnil "Created by Manus" na "Univerzita Karlova".
*   **Prezentace:** Poslal jsem mu svůj článek (17 stran) a chtěl prezentaci na konferenci. Vytvořil ji, dohledal si data na internetu, vytvořil vlastní grafy a přidal QR kód, o který jsem si řekl. Výsledek byl rovnou použitelný.
*   **Překlady se zachováním formátu:** Poslal jsem mu prezentaci o 350 slidech k překladu do angličtiny. Neudělal to tak, že by text vykopíroval, ale přímo v tom souboru přepsal texty a zachoval design.
*   **Hromadné zpracování (Deep Research):** Zadal jsem mu: *"Najdi studijní programy informatiky na všech českých vysokých školách, udělej tabulku se školným, garanty, akreditacemi..."*
    *   Manus zjistil, že existuje 8 relevantních škol.
    *   Vytvořil si 8 nezávislých "agentů" (kopií sebe sama).
    *   Každý agent prohledal web jedné fakulty.
    *   Výsledkem byla precizní Excel tabulka se všemi detaily.

### Cena a dostupnost
Manus zatím sídlí v Číně, ale přesouvá se do Singapuru. Při registraci dostanete kredity (cca 1800) a každý den se vám obnoví 300 kreditů zdarma. To stačí na menší úkoly.
Analýza tržeb stála asi 190 tokenů. Velký průzkum 17 000 záznamů mě stál v přepočtu asi 5 000 Kč, ale ušetřilo mi to měsíce práce.

## Dotazy k druhé části

**Petra Květová Pšeničná:** Tomáš se ptá: *"Kdybych chtěl projít milion webů, zvládne to Manus?"*

**Dominik Palla:** Zvládne, ale nevím, jestli to zvládne vaše peněženka. Rozdělí si to na agenty, bude to rychlé, ale drahé. Stále to ale vyjde levněji, než kdyby to dělali lidé.

**Petra Květová Pšeničná:** Matěj se ptá na srovnání s nástrojem Comet.

**Dominik Palla:** Comet je takový hybrid. Dává zajímavé odpovědi, ale je to stále beta. Často se "sekne" – ví odpověď, ale napíše, že ji neví. Manus takové chyby nedělá.

**Petra Květová Pšeničná:** Srovnání s Webflow nebo jinými nástroji na tvorbu webu?

**Dominik Palla:** U jiných nástrojů jsem vždy musel dělat odborné zásahy, opravovat chyby. Manus byl jediný, který to dotáhl do produkční podoby, která fungovala bez mých zásahů.

**Petra Květová Pšeničná:** A co srovnání s Claude nebo GitHub Copilot na programování?

**Dominik Palla:** Claude dává o chlup lepší odpovědi než ChatGPT, ale má méně funkcí. Nástroje jako Copilot jsou skvělé na napovídání kódu, ale když po nich chcete větší zásahy do aplikace, často ji "rozbijí". Nejde to pak ani spustit.

**Petra Květová Pšeničná:** Poslední dotaz na Browse AI.

**Dominik Palla:** Pokud platíte za spotřebu (tokeny), věřil bych tomu. Pokud je to za paušál nebo zdarma, bude to mít limity a velké operace to nezvládne.

## Závěr

**Petra Květová Pšeničná:** Děkuji, Dominiku, za skvělou prezentaci. Prosím účastníky o vyplnění zpětné vazby, odkaz máte v chatu.

Zvu vás na další akce:
*   **5. listopadu:** Kurz o nástroji Cursor.
*   **Listopad:** Etika a AI v praxi (citování, psaní).
*   **10. prosince:** Jak mít AI pod kontrolou a nenechat se zahltit.

Děkuji vám za pozornost a těším se příště. Hezký den.

**Dominik Palla:** Taky děkuju. Hezký den všem.