# AI Mindset - Článek pro web

## Obsah složky

```
2026-01-29_aimindset-article/
├── aimindset-final.md      ← Finální text článku
├── images/                  ← Složka s obrázky
│   ├── fail-framework-diagram.png
│   ├── komiks-clovek-bez-vs-s-ai-mindsetem.png
│   ├── meme-boromir-prompt-na-prvni-pokus.png
│   ├── meme-change-my-mind-ai-nahradi.png
│   ├── meme-distracted-boyfriend-ai-mindset.png
│   ├── meme-dve-tlacitka-rucne-vs-ai.png
│   ├── spektrum-ai-mindsetu-evoluce.png
│   ├── trikolka-ai-mindsetu-diagram.png
│   └── vibe-working-dirigent-orchestr.png
└── README.md               ← Tento soubor
```

## Jak s tím pracovat

### Text článku
Soubor `aimindset-final.md` obsahuje kompletní text článku ve formátu Markdown.

### Obrázky
V textu jsou **označená místa pro vložení obrázků** pomocí standardní Markdown syntaxe:

```markdown
![Popis obrázku](images/nazev-obrazku.png)
```

Tyto značky ukazují:
1. **Kam** v textu obrázek patří (pozice v článku)
2. **Který** obrázek použít (cesta k souboru)
3. **Alt text** pro přístupnost (text v hranatých závorkách)

### Přehled obrázků a jejich umístění

| Obrázek | Sekce v článku | Popis |
|---------|----------------|-------|
| `meme-change-my-mind-ai-nahradi.png` | Úvod (hned pod nadpisem) | "Change my mind" meme - AI tě nenahradí, nahradí tě člověk... |
| `komiks-clovek-bez-vs-s-ai-mindsetem.png` | Jak poznat člověka s AI Mindsetem | Komiks porovnávající stresovaného člověka bez AI vs klidného s AI |
| `meme-distracted-boyfriend-ai-mindset.png` | Za seznamem vlastností AI Mindsetu | "Distracted boyfriend" meme - prompt vs ruční práce |
| `spektrum-ai-mindsetu-evoluce.png` | AI Mindset Spektrum | Evoluce myšlení od základního po AI-first |
| `trikolka-ai-mindsetu-diagram.png` | AI Mindset tříkolka | Diagram tří pilířů: systémové myšlení, experimentální přístup, konverzační inteligence |
| `meme-boromir-prompt-na-prvni-pokus.png` | Neexistuje jeden správný prompt | Boromir meme - člověk nemusí napsat dokonalý prompt |
| `vibe-working-dirigent-orchestr.png` | Vibe Working | Diagram dirigent (člověk) a orchestr (AI) |
| `meme-dve-tlacitka-rucne-vs-ai.png` | Část 4: Proměna v AI-first profesionála | Meme s dvěma tlačítky - 3 hodiny ručně vs 10 minut s AI |
| `fail-framework-diagram.png` | FAIL Framework | Diagram kroků Find, Ask, Iterate, Learn |

## Pro webového vývojáře

1. **Markdown → HTML**: Převeď obsah `aimindset-final.md` do HTML struktury webu
2. **Obrázky**: Nahraj obrázky ze složky `images/` na web a uprav cesty v HTML
3. **Responzivita**: Obrázky jsou různých velikostí, zajisti responzivní zobrazení
4. **Alt texty**: V Markdown jsou již připravené alt texty pro přístupnost

## Odkazy v článku

V článku jsou již doplněné odkazy na služby a produkty Aibility a Filipa Dřímalky:

| Služba/Produkt | URL |
|---------------|-----|
| Future AI Leader Masterclass | https://drimalka.com/masterclass/ |
| Aimee (AI Coach) | https://aibility.cz/aimee |
| Test AI dovedností | https://aibility.cz/aidovednosti |
| Aibility Club | https://aibility.cz/club |
| Podcast Budoucnost nepráce | https://www.youtube.com/@drimalkafilip/videos |
| Filip Dřímalka (LinkedIn) | https://www.linkedin.com/in/drimalka/ |
| Kniha Budoucnost nepráce | https://drimalka.com/neprace/ |
| Aibility (homepage) | https://aibility.cz |

## Poznámky

- Obrázky jsou ve formátu PNG
- Všechny obrázky byly vygenerovány pomocí AI (Gemini), zůstává na nich Gemini vodoznak
- Některé obrázky jsou memes, některé jsou infografiky/diagramy
- V článku je na konci placeholder pro email formulář - bude potřeba dopracovat
