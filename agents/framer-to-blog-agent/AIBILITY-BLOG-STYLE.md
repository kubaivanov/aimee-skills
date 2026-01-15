# Aibility Blog - Vizuální styl pro generování obrázků

## 🎨 Charakteristika stylu

Obrázky na Aibility blogu mají specifický vizuální jazyk:

| Vlastnost | Popis |
|-----------|-------|
| **Typ** | Fotorealistické snímky |
| **Subjekt** | Lidé pracující s technologií |
| **Kompozice** | Často z profilu nebo zezadu |
| **Pozadí** | Měkké, rozmazané (bokeh efekt) |
| **Barevnost** | Pastelové tóny - fialová, růžová, tyrkysová |
| **Atmosféra** | Snová, profesionální ale lidská |
| **Prostředí** | Moderní kancelář, startup, coworking |

---

## 📁 Referenční obrázky

Uložené v:
```
/Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen/reference-images/
```

| Soubor | Popis |
|--------|-------|
| `01-lide-ve-startupu.png` | Lidé ve startupu, fialové tóny |
| `04-vibe-coding-generated.png` | Vygenerovaný obrázek ve správném stylu |

---

## 🚀 Jak generovat obrázky

### Základní příkaz

```bash
cd /Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen

python3 generate.py "PROMPT" --ref reference-images/01-lide-ve-startupu.png
```

### Master prompt šablona

```
A person [AKCE] in modern office, soft dreamy aesthetic, pastel purple and cyan tones, 
slightly blurred background, professional but warm atmosphere, photorealistic style, 
person seen from side or back, [KONTEXT ČLÁNKU]
```

---

## 📝 Příklady promptů podle témat

### Pro články o kódování/programování
```
A person coding on laptop in modern office, soft dreamy aesthetic, pastel purple and cyan tones, slightly blurred background, professional but warm atmosphere, photorealistic style, person seen from side or back, creating software with AI assistance
```

### Pro články o AI nástrojích
```
A professional working with AI tools on computer screen, soft dreamy aesthetic, pastel purple and pink tones, slightly blurred background, modern startup office, person seen from side, focused and productive atmosphere
```

### Pro články o týmové spolupráci
```
Team collaborating in modern coworking space, soft dreamy aesthetic, pastel purple and cyan tones, blurred background with warm lighting, people discussing around laptops, professional but friendly atmosphere
```

### Pro články o automatizaci
```
A person setting up automated workflows on dual monitors, soft dreamy aesthetic, pastel purple tones, slightly blurred modern office background, professional atmosphere, person seen from back, digital transformation concept
```

### Pro články o HR/náboru
```
A HR professional conducting interview in modern office, soft dreamy aesthetic, pastel purple and warm tones, blurred background, professional and welcoming atmosphere, two people talking
```

### Pro články o produktivitě
```
A focused professional working efficiently on laptop, soft dreamy aesthetic, pastel pink and purple tones, cozy modern workspace, slightly blurred background, person seen from side, calm productive atmosphere
```

---

## 🔧 Cursor instrukce

Když uživatel řekne:
- "Vygeneruj obrázek pro článek o [TÉMA]"
- "Udělej vizuál k článku"
- "Potřebuji header image pro blog"

### Postup:

1. **Analyzuj téma článku** a vyber vhodný prompt z šablon výše

2. **Spusť generování s referencí:**
```bash
cd /Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen

python3 generate.py "[UPRAVENÝ PROMPT]" --ref reference-images/01-lide-ve-startupu.png
```

3. **Zobraz výsledek** uživateli

4. **Pokud není spokojen**, uprav prompt a vygeneruj znovu

---

## ⚠️ Co NEDĚLAT

- ❌ Abstraktní ilustrace (nejsou ve stylu Aibility)
- ❌ Obrázky bez lidí
- ❌ Příliš syté/křiklavé barvy
- ❌ Technické diagramy nebo infografiky
- ❌ Stock photo vzhled (příliš posed, falešné úsměvy)

## ✅ Co DĚLAT

- ✅ Vždy používat referenční obrázek
- ✅ Zachovat měkkou, snovou estetiku
- ✅ Fialové/růžové/tyrkysové tóny
- ✅ Lidé v přirozeném pracovním prostředí
- ✅ Rozmazané pozadí s bokeh efektem

---

## 📂 Cesty k souborům (pro Cursor)

```
Nástroj:     /Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen/generate.py
Reference:   /Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen/reference-images/01-lide-ve-startupu.png
Výstupy:     /Users/veronikapaulusova/Documents/POWER-PLACE/projects-2026/aibility-26/blog-strategie/gemini-image-gen/images/
```

---

## 🎯 Quick command

Pro rychlé generování stačí říct Cursoru:

```
Vygeneruj obrázek pro článek "[NÁZEV ČLÁNKU]" ve stylu Aibility blogu.
Použij @blog-strategie/gemini-image-gen s referencí.
```

Cursor automaticky:
1. Vytvoří prompt podle tématu
2. Použije správnou referenci
3. Vygeneruje obrázek
4. Zobrazí výsledek

---

Vytvořeno: 13.1.2026
Poslední aktualizace: 13.1.2026
