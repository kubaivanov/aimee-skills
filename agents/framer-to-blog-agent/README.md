# Aibility Framer-to-Blog Agent 🚀

Tato složka obsahuje nástroje pro plně automatizované nasazování článků na blog Aibility ve Frameru.

## Co to umí?
Vezme článek v HTML, automaticky k němu vygeneruje obrázek v Aibility stylu, nahraje ho na GitHub (pro trvalý hosting) a připraví data pro nahrání do Framer CMS.

## Struktura
- `deploy.py`: Hlavní spouštěcí skript.
- `scripts/`: Pomocné skripty pro generování obrázků a nahrávání na GitHub.
- `reference-images/`: Referenční obrázky pro zachování stylu.
- `images/`: Lokální archiv vygenerovaných obrázků.
- `AIBILITY-BLOG-STYLE.md`: Definice vizuálního stylu Aibility.

## Jak to použít (pro Cursor Agent)
1. Uživatel ti dá článek (např. v `clanky/`).
2. Spusť skript: `python3 deploy.py path/to/article.md`.
3. Skript vygeneruje obrázek, pushne ho na GitHub a vytvoří `.json` soubor.
4. Požádej uživatele o aktuální **Framer MCP SSE URL** z pluginu Unframer (uživatel musí mít otevřený Framer a spuštěný plugin).
5. Nahraj článek do CMS pomocí: `python3 scripts/framer_upsert.py path/to/article.json "SSE_URL"`.

## Požadavky
- Python 3.x
- Nainstalované balíčky z `requirements.txt` (`pip install -r requirements.txt`)
- `.env` soubor s `OPENROUTER_API_KEY`.
- Přístup ke GitHub repu `aibilitycz/web-assets-hosting`.
- **Otevřený Framer projekt** a spuštěný **Unframer (MCP) plugin**.
  - *Tip: Pokud nevíte, co to je nebo jak to spustit, zeptejte se Cursoru, rád vám s nastavením pomůže.*
