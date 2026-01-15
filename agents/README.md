# 🤖 Aibility AI Agents & Tools

Tato složka obsahuje specializované AI agenty a nástroje pro automatizaci obsahu projektu Aibility. Každý nástroj je samostatný celek s vlastní konfigurací a instrukcemi.

---

## 📋 Seznam agentů a nástrojů

### 🧹 agent-cistic-prepisu (v1.0)
Nástroj pro inteligentní čištění surových přepisů webinářů.
- **Funkce:** Odstraňuje časové značky, výplňová slova a balast, zatímco zachovává veškeré know-how, jména mluvčích a příklady. Formátuje text do logických celků.
- **Modely:** Gemini 3 Pro (primární) + Claude Opus 4.5 (fallback).
- **Použití:** `python3 skript/cistic-prepisu.py <vstup> <vystup>`

### ✍️ agent-copywriter-blog-prepisy (v1.0)
Specializovaný copywriter pro tvorbu blogových článků z vyčištěných přepisů.
- **Funkce:** Analyzuje přepis a v jednom kroku vytvoří 3 různé varianty článků (A, B, C) s odlišným úhlem pohledu. Píše v lidském, lektorském stylu Aibility.
- **Výstup:** Tři samostatné Markdown články připravené k editaci.
- **Použití:** `python3 skript/copywriter.py <cesta_k_prepisu>`

### 🚀 framer-to-blog-agent (v1.0)
Automatizovaný „nasazovač“ článků přímo do Framer CMS.
- **Funkce:** Převede článek na formát pro Framer, vygeneruje k němu AI ilustraci v Aibility stylu (přes Gemini) a nahraje ji na GitHub hosting. Následně nahrává data přímo do CMS přes MCP endpoint.
- **Klíčová vlastnost:** Obejítí limitů Cursoru pomocí přímého nahrávání přes SSE plugin Unframer.
- **Použití:** `python3 deploy.py <clanek.md>` následované `python3 scripts/framer_upsert.py <metadata.json> "SSE_URL"`

---

## 🛠️ Správa verzí
Při každé významné změně v logice skriptů, instrukcích agenta (`AGENTS.md`) nebo struktuře nástroje, prosím, aktualizujte verzi v tomto README:
- **v1.x** -> drobné úpravy, opravy chyb, aktualizace promptů.
- **v2.x** -> velké změny v architektuře, změna modelů nebo přidání zásadních funkcí.

---

## 🔑 Společné požadavky
Většina nástrojů vyžaduje:
1. **Python 3.x** a instalaci závislostí z `requirements.txt`.
2. **OpenRouter API klíč** uložený v souboru `.env` v příslušné složce skriptu.
3. Přístup k repozitáři **aibilitycz/web-assets-hosting** pro hosting obrázků.
