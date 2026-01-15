# Instrukce pro Cursor: Vkládání webinářů

## Kdy použít

Když uživatel řekne něco jako:
- "Vlož webinář z @soubor.html do Frameru"
- "Nasaď tento webinář do CMS"
- "Přidej webinář do kolekce Webináře"

---

## Postup

### 1. Přečti HTML soubor
- Metadata jsou v HTML komentáři na začátku (`<!-- ... -->`)
- HTML obsah je pod metadaty

### 2. Parsuj metadata
Každý řádek v komentáři má formát `klíč: hodnota`

### 3. Rozděl HTML sekce
- `<section id="uvodni-popisek">` → pole `cJixpFOWT`
- `<section id="o-cem-webinar">` → pole `JsnsK33lL`

### 4. Převeď enum hodnoty
Použij mapování z README.md:
- "Placené" → "QvM2vy9qy"
- "Začátečník" → "o9nwhjtn1"
- atd.

### 5. Převeď lektory na ID
Pro pole `lektori`:
1. Zavolej `getCMSItems` na kolekci Lektoři (Qv5ijP6Gb)
2. Najdi lektory podle jména
3. Použij jejich item ID

### 6. Zavolej upsertCMSItem

```json
{
  "collectionId": "X1L5HIkFg",
  "slug": "hodnota-z-metadat",
  "draft": true,
  "fieldData": {
    "ziIxHT3eC": {"type": "string", "value": "..."},
    "uazEqpXke": {"type": "string", "value": "..."},
    ...
  }
}
```

---

## Formát fieldData

Každé pole musí být objekt s `type` a `value`:

```json
{
  "fieldId": {"type": "string", "value": "text"},
  "fieldId": {"type": "number", "value": 1990},
  "fieldId": {"type": "boolean", "value": true},
  "fieldId": {"type": "date", "value": "2025-02-15T00:00:00.000Z"},
  "fieldId": {"type": "image", "value": "https://url.jpg"},
  "fieldId": {"type": "enum", "value": "enumOptionId"},
  "fieldId": {"type": "formattedText", "value": "<p>HTML</p>"},
  "fieldId": {"type": "multiCollectionReference", "value": ["itemId1", "itemId2"]}
}
```

---

## Checklist před vložením

- [ ] Všechna povinná pole vyplněna
- [ ] Datum ve formátu ISO 8601
- [ ] Enum hodnoty převedeny na ID
- [ ] Lektoři převedeni na item ID
- [ ] Slug je unikátní (bez diakritiky, malá písmena, pomlčky)

---

## Mapování metadat → Field ID

| Metadata klíč | Field ID |
|---------------|----------|
| nazev | ziIxHT3eC |
| id_webinare | uazEqpXke |
| kratky_popisek | TanbAFOpe |
| obrazek | InaMMUD7z |
| co_si_odnesete | zRxj2Lur0 |
| pro_koho | aTzZ_Yi1z |
| pozadavky | idQA0EJvA |
| co_ziskate | DlJuiHxqn |
| lektori | y3nFTLKQe |
| zobrazit_testimonials | e1XlEUGt6 |
| zobrazit_faq | EanDkRlnr |
| faq | TrzUwp1SO |
| uroven | iIWFsHpdJ |
| link_na_kurz | Xezk3Pe3y |
| online | B3AEb_QUo |
| mesto | Gkn2CMJyS |
| adresa | D8jvUc0Pb |
| datum_konani | pLSofYvBJ |
| delka_trvani | ax8QiwxlJ |
| monetizace | ISJJ93kqM |
| soucasti_edu_stream | MfWHFjoCx |
| cena | KnpoA9sRg |
| simpleshop_id | CIly7uWDj |
| simpleshop_link | cO8NQUMhD |
| zverejneno | rJC7SVOUc |
| zobrazit_v_probehlych | EsTq1D2u4 |
| zahrnout_na_uvodni | OICEIjpYO |
| pripravujeme | PsglP_sYG |

---

## Enum mapování

### monetizace → ISJJ93kqM
- Placené → QvM2vy9qy
- Zdarma → kVPCzKf9p
- Pouze AI Edu Stream → AdeflBgmW

### uroven → iIWFsHpdJ
- Začátečník → o9nwhjtn1
- Mírně pokročilé → fFSpPLDPI
- Středně pokročilé → GLNNRrtba
- Pokročilé → gnGYKfdfH
- Super pokročilé → R8Xohh505
