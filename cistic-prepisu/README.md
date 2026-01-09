# 🧹 Cistic prepisu webinaru

Automatický nástroj pro vyčištění přepisů webinářů pomocí Gemini 3 Pro Preview (primárně) a Claude Opus 4.5 (fallback) přes OpenRouter API s automatickým fallbackem mezi modely.

## 📋 Pozadavky

- Python 3.7+
- OpenRouter API klic

## 🚀 Instalace

1. Nainstaluj zavislosti:
```bash
cd skript
pip install -r requirements.txt
```

2. Nastav svůj API klíč:
   - Ve složce `skript/` najdeš soubor `.env.example`.
   - Přejmenuj ho na `.env` (nebo ho vytvoř).
   - Vlož do něj svůj klíč: `OPENROUTER_API_KEY=tvuj_klic`
   - Tento soubor je ignorován gitem, takže tvůj klíč zůstane v bezpečí.

## 💻 Pouziti

### Zpracovani jednoho prepisu

Skript bere dva argumenty: vstupní a výstupní soubor:

```bash
python3 skript/cistic-prepisu.py \
  "prepisy-webinaru/nazev-prepisu.md" \
  "vycistene-prepisy-webinaru/nazev-prepisu-vycisteny.md"
```

### Co skript dela

- **Odstraňuje:** časové značky (`[00:42]`, `[01:15:30]`), organizační poznámky („pište do chatu", „záznam pošleme"), výplňová slova („eh", „hm", „no", „prostě", „jakoby") - jen pokud nenesou význam, překlepy a neukončené věty
- **Zachovává:** veškerý obsahový obsah, myšlenky, příklady, analogie, dotazy a odpovědi, humor a osobní poznámky, jména mluvčích
- **Formátuje:** rozdělí do logických odstavců, přidá nadpisy podle průběhu (Uvod, Hlavni cast, Diskuse, Zaver)
- **Nikdy nezkracuje** ani neshrnuje obsah

### Format nazvu souboru

- Původní: `cursor-v-praxi-5.11.2025-prepis.md`
- Vyčištěný: `cursor-v-praxi-5.11.2025-prepis-vycisteny.md`

## ⚙️ Konfigurace

V souboru `skript/cistic-prepisu.py` můžeš upravit:

- `MODELS` - seznam modelů s prioritou (výchozí: `google/gemini-3-pro-preview`, fallback: `anthropic/claude-opus-4.5`)
- `MAX_CHUNK_SIZE` - maximální velikost textu pro jeden request (výchozí: 80000 znaků)
- `MAX_PARALELNICH` - počet částí zpracovávaných paralelně (výchozí: 5)

### Automaticky fallback mezi modely

Skript automaticky:
- **Primárně používá:** `google/gemini-3-pro-preview` (Gemini 3 Pro Preview - rychlejší)
- **Fallback:** `anthropic/claude-opus-4.5` (Claude Opus 4.5)

Pokud primární model není dostupný (high demand, 404, timeout), skript automaticky přepne na fallback model.

### Paralelni zpracovani

Skript automaticky rozdělí dlouhé přepisy na části a zpracuje je paralelně (maximálně 5 současně), což výrazně zrychluje zpracování velkých souborů.

## 📝 Poznamky

- Skript automaticky rozdělí dlouhé přepisy na části, aby se vešly do limitu API
- Instrukce pro čištění se načítají z `AGENTS.md` (sekce "Pravidla pro cisteni")
- Skript automaticky detekuje nedostupnost modelu (high demand, 404, timeout) a přepne na fallback
- Paralelní zpracování zrychluje zpracování velkých přepisů

## 🔍 Kontrola dostupnych modelu

Pokud chceš použít jiné modely nebo ověřit dostupné modely, zkontroluj:
- [OpenRouter Models](https://openrouter.ai/models)
- Aktuální názvy modelů mohou být různé - uprav je v seznamu `MODELS` v souboru `skript/cistic-prepisu.py`
