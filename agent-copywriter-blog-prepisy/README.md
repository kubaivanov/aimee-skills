# ✍️ Copywriter: Blogove clanky z prepisu

Tento AI agent je specializovaný na transformaci vyčištěných přepisů webinářů do tří různých variant vzdělávacích blogových článků pro projekt Aibility.

## 📋 Jak to funguje

Agent pracuje ve dvou krocích:
1.  **Analyza a mapovani:** Identifikuje hlavní témata a navrhne 3 různé úhly pohledu (varianty A, B, C).
2.  **Tvorba clanku:** Vygeneruje tři kompletní texty připravené k publikaci.

## 📂 Struktura slozky

- `AGENTS.md` - Kompletní systémové instrukce pro AI agenta.
- `priklady-skvelych-clanku/` - Referenční texty pro zachování tónu a stylu.
- `clanky-k-editaci/` - Výstupní složka pro vygenerované články.

## 🚀 Jak pouzivat

1.  Měj připravený vyčištěný přepis webináře.
2.  Spusť generování pomocí skriptu:
    ```bash
    python3 skript/copywriter.py "cesta/k/vycistenemu-prepisu.md"
    ```
3.  Agent automaticky vytvoří tři varianty článků a uloží je do složky `clanky-k-editaci/`.

## ⚙️ Nastaveni API (OpenRouter)

1.  Přejdi do složky `skript/`.
2.  Zkopíruj `.env.example` na `.env`.
3.  Vlož svůj OpenRouter API klíč do `.env`: `OPENROUTER_API_KEY=tvuj_klic`.

## 🗣️ Ton a styl

- Lidský, srozumitelný a inspirativní.
- Role lektora, který předává know-how.
- Bez korporátního žargonu a výplňových slov.
- Přímé oslovení čtenáře (vy).

## 📝 Poznamky

- Výsledné články by měly být uloženy ve formátu Markdown s názvem: `YYYY-MM-DD-Varianta-nazev-clanku.md`.
- Agent nikdy nezmiňuje, že text vychází z webináře – články musí fungovat samostatně.
