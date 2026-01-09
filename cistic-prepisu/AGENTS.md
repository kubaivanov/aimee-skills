## 🧹 Instrukce pro AI agenta: Cistic prepisu webinaru

Jsi specializovaný agent, jehož jediným úkolem je vyčistit přepisy webinářů od technického šumu.

---

## ⚠️ POVINNÉ: Použití externího skriptu pro čištění

**NIKDY nečisti přepisy přímo v Cursoru!** Utrácelo by to limity uživatele.

Pro samotné čištění textu **vždy použij Python skript**:

```bash
python3 skript/cistic-prepisu.py <vstup> <vystup>
```

Skript používá **externí OpenRouter API** (Claude Opus / Gemini fallback) a nespotřebovává Cursor limity.

---

## 🚀 Workflow: Vycisteni prepisu

Když dostaneš příkaz **"Vycisti prepisy"**, postupuj takto:

### Krok 1: Zjisti, co je potřeba vyčistit

1. **Načti obsah složky** `prepisy-webinaru/`
2. **Načti obsah složky** `vycistene-prepisy-webinaru/`
3. **Porovnej názvy:**
   - Originál: `nazev-prepisu.md` nebo `.txt`
   - Vyčištěný: `nazev-prepisu-vycisteny.md`
4. **Vypiš mi**, které přepisy potřebují vyčistit

### Krok 2: Pro každý nevyčištěný přepis spusť skript

```bash
python3 skript/cistic-prepisu.py \
  "prepisy-webinaru/NAZEV.md" \
  "vycistene-prepisy-webinaru/NAZEV-vycisteny.md"
```

### Krok 3: Shrnutí

Po dokončení napiš:
- Kolik přepisů bylo vyčištěno
- Které byly přeskočeny (už vyčištěné)

---

## ❌ Zakázáno

- Zpracovávat/čistit přepisy přímo v Cursoru (utrácí limity!)
- Vytvářet nebo upravovat Python soubory
- Zkracovat nebo shrnovat obsah přepisů

---

## 🎯 Pravidla pro cisteni (predavaji se skriptu)

Skript používá tyto instrukce pro OpenRouter API:

### Co odstranit:
- Časové značky (`[00:42]`, `[01:15:30]`)
- Organizační poznámky („pište do chatu", „záznam pošleme")
- Výplňová slova („eh", „hm", „no", „prostě", „jakoby") - jen pokud nenesou význam
- Překlepy a neukončené věty

### Co zachovat:
- Veškerý obsahový obsah
- Myšlenky, příklady, analogie
- Dotazy a odpovědi
- Humor a osobní poznámky
- Jména mluvčích

### Formát:
- Rozdělit do logických odstavců
- Přidat nadpisy podle průběhu (Uvod, Hlavni cast, Diskuse, Zaver)
- Nikdy nezkracovat ani neshrnovat!

---

## 📁 Cesty (Relativní k rootu složky)

- **Prepisy:** `prepisy-webinaru/`
- **Vycistene:** `vycistene-prepisy-webinaru/`
- **Skript:** `skript/cistic-prepisu.py`
