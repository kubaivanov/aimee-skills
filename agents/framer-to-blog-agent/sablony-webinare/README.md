# Webináře - Framer CMS struktura

## Collection ID
```
X1L5HIkFg
```

---

## Pole

| Metadata klíč | Field ID | Typ | Povinné |
|---------------|----------|-----|---------|
| nazev | ziIxHT3eC | string | ✅ |
| id_webinare | uazEqpXke | string | ✅ |
| kratky_popisek | TanbAFOpe | string | ✅ |
| obrazek | InaMMUD7z | image | ❌ |
| uvodni_popisek | cJixpFOWT | formattedText | ✅ |
| o_cem_webinar | JsnsK33lL | formattedText | ✅ |
| co_si_odnesete | zRxj2Lur0 | string | ✅ |
| pro_koho | aTzZ_Yi1z | string | ✅ |
| pozadavky | idQA0EJvA | string | ✅ |
| co_ziskate | DlJuiHxqn | string | ✅ |
| lektori | y3nFTLKQe | multiCollectionReference | ✅ |
| zobrazit_testimonials | e1XlEUGt6 | boolean | ❌ |
| zobrazit_faq | EanDkRlnr | boolean | ❌ |
| faq | TrzUwp1SO | string | ❌ |
| uroven | iIWFsHpdJ | enum | ❌ |
| link_na_kurz | Xezk3Pe3y | link | ❌ |
| online | B3AEb_QUo | boolean | ❌ |
| mesto | Gkn2CMJyS | string | ❌ |
| adresa | D8jvUc0Pb | string | ❌ |
| datum_konani | pLSofYvBJ | date | ❌ |
| delka_trvani | ax8QiwxlJ | number | ❌ |
| monetizace | ISJJ93kqM | enum | ❌ |
| soucasti_edu_stream | MfWHFjoCx | boolean | ❌ |
| cena | KnpoA9sRg | number | ❌ |
| simpleshop_id | CIly7uWDj | string | ❌ |
| simpleshop_link | cO8NQUMhD | link | ❌ |
| zverejneno | rJC7SVOUc | boolean | ❌ |
| zobrazit_v_probehlych | EsTq1D2u4 | boolean | ❌ |
| zahrnout_na_uvodni | OICEIjpYO | boolean | ❌ |
| pripravujeme | PsglP_sYG | boolean | ❌ |

---

## Enum hodnoty

### Monetizace (ISJJ93kqM)
| Píšeš | Framer ID |
|-------|-----------|
| Placené | QvM2vy9qy |
| Zdarma | kVPCzKf9p |
| Pouze AI Edu Stream | AdeflBgmW |

### Úroveň adopce AI (iIWFsHpdJ)
| Píšeš | Framer ID |
|-------|-----------|
| Začátečník | o9nwhjtn1 |
| Mírně pokročilé | fFSpPLDPI |
| Středně pokročilé | GLNNRrtba |
| Pokročilé | gnGYKfdfH |
| Super pokročilé | R8Xohh505 |

---

## Lektoři (reference)

Pole `lektori` odkazuje na kolekci **Lektoři** (ID: `Qv5ijP6Gb`).

V metadatech piš jména lektorů oddělená čárkou:
```
lektori: Filip Dřímalka, Jana Novák
```

Cursor najde jejich ID v CMS automaticky.

---

## FormattedText sekce

V šabloně jsou dvě HTML sekce pro formattedText pole:

1. `<section id="uvodni-popisek">` → pole `cJixpFOWT`
2. `<section id="o-cem-webinar">` → pole `JsnsK33lL`

---

## Příklad použití

```
Vezmi webinář z @sablony-webinare/muj-webinar.html 
a vlož ho do Framer CMS.

Použij Collection ID: X1L5HIkFg
Mapování polí najdeš v @sablony-webinare/README.md
```

---

## Poznámky

- **Draft**: Cursor vkládá jako draft, publikuješ ručně
- **Obrázek**: Používej placeholder, vyměníš ve Frameru
- **Lektoři**: Musí existovat v CMS kolekci Lektoři
