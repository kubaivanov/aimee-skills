# Návod: Jak vytvořit šablonu pro jakékoliv Framer CMS

Tento návod ti ukáže, jak si připravit šablonu pro rychlé vkládání obsahu do libovolné CMS kolekce ve Frameru (blog, webináře, lektoři, testimonials...).

---

## 🎯 Co potřebuješ

1. **Cursor** (AI editor)
2. **Framer projekt** s CMS kolekcí
3. **Framer MCP plugin** (v Frameru: Cmd+K → "MCP")

---

## 📋 Krok 1: Zjisti strukturu CMS kolekce

### Otevři Framer MCP plugin
1. Otevři svůj Framer projekt
2. Stiskni **Cmd+K**
3. Napiš **"MCP"** a otevři plugin
4. Nech plugin otevřený (zelená tečka = připojeno)

### Požádej Cursor o strukturu
V Cursoru napiš:

```
Zjisti strukturu CMS kolekce "Webináře" ve Frameru.
Potřebuji vědět:
- Collection ID
- Všechna pole (field ID, název, typ, povinnost)
- U enum polí seznam možných hodnot
```

Cursor ti vrátí něco jako:

```
Collection ID: X1L5HIkFg

Pole:
- ziIxHT3eC: Název (string, povinné)
- uazEqpXke: ID webináře (string, povinné)
- TanbAFOpe: Krátký popisek (string, povinné)
- InaMMUD7z: Abstraktní obrázek (image)
- cJixpFOWT: Úvodní popisek (formattedText, povinné)
...
```

---

## 📝 Krok 2: Vytvoř HTML šablonu

Vytvoř soubor, např. `sablony/webinar-TEMPLATE.html`:

```html
<!--
METADATA (pro Cursor)
slug: nazev-v-url
nazev: Název webináře
id_webinare: ABC123
kratky_popisek: Krátký popis pro kartu
obrazek: https://framerusercontent.com/images/PLACEHOLDER.png
datum_konani: 2025-02-15
online: true
mesto: Praha
cena: 1990
monetizace: Placené
uroven: Začátečník
-->

<h2>Úvodní popisek</h2>
<p>Text úvodního popisku...</p>

<h2>O čem je tento webinář?</h2>
<p>Detailní popis webináře...</p>
```

### Pravidla pro metadata:
- Každé pole na vlastní řádek
- Formát: `nazev_pole: hodnota`
- Pro enum pole piš **česky** (Cursor převede na ID)
- Pro boolean piš `true` nebo `false`
- Pro datum piš `YYYY-MM-DD`

---

## 📄 Krok 3: Vytvoř README s mapováním

Vytvoř `sablony/webinar-README.md`:

```markdown
# Webináře - CMS struktura

## Collection ID
X1L5HIkFg

## Pole

| Metadata klíč | Field ID | Typ | Povinné |
|---------------|----------|-----|---------|
| nazev | ziIxHT3eC | string | ✅ |
| id_webinare | uazEqpXke | string | ✅ |
| kratky_popisek | TanbAFOpe | string | ✅ |
| obrazek | InaMMUD7z | image | ❌ |
| uvodni_popisek | cJixpFOWT | formattedText | ✅ |
| o_cem_webinar | JsnsK33lL | formattedText | ✅ |
| datum_konani | pLSofYvBJ | date | ❌ |
| online | B3AEb_QUo | boolean | ❌ |
| cena | KnpoA9sRg | number | ❌ |

## Enum hodnoty

### Monetizace (ISJJ93kqM)
| Píšeš | ID |
|-------|-----|
| Placené | QvM2vy9qy |
| Zdarma | kVPCzKf9p |
| Pouze AI Edu Stream | AdeflBgmW |

### Úroveň adopce AI (iIWFsHpdJ)
| Píšeš | ID |
|-------|-----|
| Začátečník | o9nwhjtn1 |
| Mírně pokročilé | fFSpPLDPI |
| Pokročilé | gnGYKfdfH |
```

---

## 🚀 Krok 4: Použití šablony

### Vytvoř nový obsah
1. Zkopíruj šablonu: `webinar-TEMPLATE.html` → `webinar-muj-novy.html`
2. Vyplň metadata a HTML obsah
3. Ulož soubor

### Vlož do Frameru
V Cursoru napiš:

```
Vezmi webinář z @sablony/webinar-muj-novy.html 
a vlož ho do Framer CMS kolekce "Webináře".

Použij:
- Collection ID: X1L5HIkFg
- Mapování polí z @sablony/webinar-README.md
```

---

## 💡 Tipy pro efektivitu

### 1. Placeholder obrázek
Nastav si jeden univerzální placeholder obrázek:
```
obrazek: https://framerusercontent.com/images/2WraAH3ZmKAKqfi8sN7YfZ2v3Qs.png
```
Pak ho ve Frameru ručně vyměníš.

### 2. Draft vs. publikováno
Cursor standardně vkládá jako **draft** (koncept). Publikuješ pak ručně ve Frameru.

### 3. Více položek najednou
Můžeš připravit více souborů a říct Cursoru:
```
Vlož všechny webináře ze složky @sablony/webinare/ do Framer CMS.
```

### 4. Reference na jiné kolekce
Pro pole typu `multiCollectionReference` (např. Lektoři):
```
lektori: Filip Novák, Jana Svobodová
```
Cursor najde jejich ID v CMS automaticky.

---

## 🔧 Řešení problémů

### "Framer MCP neodpovídá"
→ Otevři Framer, Cmd+K, "MCP", počkej na zelenou tečku

### "Field is required"
→ Zkontroluj, že máš vyplněná všechna povinná pole (✅ v README)

### "Invalid enum value"
→ Zkontroluj, že píšeš přesně hodnoty z README (česky, s diakritikou)

### "Slug already exists"
→ Změň slug na unikátní hodnotu

---

## 📚 Příklad: Kompletní workflow

```
1. Mám nový webinář
2. Zkopíruji šablonu → webinar-ai-pro-hr.html
3. Vyplním metadata a obsah
4. V Cursoru: "Vlož @webinar-ai-pro-hr.html do Framer CMS Webináře"
5. Cursor to vloží jako draft
6. Ve Frameru zkontroluju a publikuju
```

**Celý proces: ~2 minuty** ⚡

---

## 🎨 Podporované typy polí

| Typ | Jak psát v metadatech |
|-----|----------------------|
| string | `nazev: Můj text` |
| number | `cena: 1990` |
| boolean | `online: true` |
| date | `datum: 2025-02-15` |
| image | `obrazek: https://url.jpg` |
| link | `odkaz: https://example.com` |
| enum | `kategorie: Název možnosti` (česky) |
| formattedText | Celý HTML obsah pod metadaty |

---

Vytvořeno pro Aibility tým 💜
