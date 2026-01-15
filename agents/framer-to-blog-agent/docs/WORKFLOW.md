# Workflow: Článek → Framer CMS

## Nejrychlejší cesta (doporučeno)

### 1. Napiš článek v HTML

Vytvoř soubor `clanky/muj-clanek.html` podle šablony `clanky/TEMPLATE.html`.

Metadata v komentáři na začátku:
```html
<!--
METADATA
slug: muj-novy-clanek
title: Můj nový článek o AI
date: 2025-01-13
category: Business
featured: false
preview: První věta článku pro náhled.
image: https://url-obrazku.jpg
-->
```

### 2. Dej článek Cursoru

Prompt:
```
Vezmi článek z @clanky/muj-clanek.html a vlož ho do Framer CMS blogu.
Použij upsertCMSItem s collectionId "A7DWNZVX_".
```

Cursor automaticky:
- Přečte metadata z komentáře
- Převede kategorii na správné ID
- Vytvoří JSON s fieldData
- Zavolá Framer MCP

---

## Alternativa: Rovnou JSON

Pokud preferuješ mít vše v jednom souboru:

```
Vlož tento článek do Framer CMS:

{
  "slug": "...",
  "fieldData": { ... }
}
```

---

## Tipy pro rychlost

1. **Obrázky** - nahrávej předem do Frameru a kopíruj URL
2. **Datum** - stačí napsat `2025-01-13`, Cursor převede na ISO
3. **Kategorie** - piš česky (Business, Nástroje...), Cursor převede na ID

## Mapping kategorií

| Píšeš | Cursor použije |
|-------|----------------|
| Business | `ErKWS9XfT` |
| Nástroje | `RwPb_GhT4` |
| Tutoriál | `BRGN6RAJs` |
| Case Study | `ViXT0FDf0` |
| Etika | `AZtKTmohl` |
| HR | `NdjRdNX15` |
