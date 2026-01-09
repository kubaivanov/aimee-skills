# 🔍 Jak overit, ze se pouziva externi OpenRouter API (ne Cursor tokeny)

## ✅ Zpusoby overeni

### 1. **Vystup skriptu pri behu**

Když spustíš skript, uvidíš jasné indikátory:

```
🧹 Cistic prepisu webinaru
==================================================
🌐 Pouziva OpenRouter API (externi modely, ne Cursor tokeny)
==================================================
📥 Nacitam OpenRouter API klic...
✅ OpenRouter API klic nacten (zacatek: sk-or-v1-...)
🔍 Kontroluji dostupnost modelu...
   🌐 Volam OpenRouter API (test dostupnosti)...
   📡 Odpoved z OpenRouter: 200
✅ Model anthropic/claude-3-opus je dostupny pres OpenRouter
```

Při zpracování přepisů uvidíš:
```
🌐 Volam OpenRouter API - model: anthropic/claude-3-opus
✅ Odpoved z OpenRouter - pouzito: 1234 tokenu
```

### 2. **OpenRouter Dashboard**

1. Přihlas se na https://openrouter.ai
2. Jdi do **Activity** nebo **Usage**
3. Uvidíš všechny requesty v reálném čase:
   - Který model byl použit
   - Kolik tokenů bylo spotřebováno
   - Čas requestu
   - Náklady

**Pokud tam žádné requesty nejsou** → skript nefunguje správně nebo se používá něco jiného.

### 3. **Kontrola API klice**

Skript načítá API klíč buď z proměnné prostředí `OPENROUTER_API_KEY`, nebo ze souboru `.env` či `.api_key` ve stejné složce jako skript.

Pokud tento soubor neexistuje nebo je prázdný, skript se zastaví s chybou.

### 4. **Network monitoring (pokrocile)**

Můžeš zkontrolovat, že se volá správný endpoint:
- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Pokud by se používaly Cursor tokeny, volalo by se jiné API

## 🚨 Jak poznat, ze se NEPOUZIVA OpenRouter

**Varovne signaly:**
- ❌ Ve výstupu není "🌐 Volam OpenRouter API"
- ❌ V OpenRouter dashboardu nejsou žádné requesty
- ❌ Skript běží, ale v OpenRouter není žádná aktivita
- ❌ Chybí zpráva "✅ Odpoved z OpenRouter"

## ✅ Jak poznat, ze se POUZIVA OpenRouter

**Pozitivni signaly:**
- ✅ Ve výstupu vidíš "🌐 Volam OpenRouter API"
- ✅ V OpenRouter dashboardu jsou requesty
- ✅ Vidíš informace o spotřebě tokenů
- ✅ Skript ukazuje, který model se používá

## 📊 Testovaci prikaz

Pro rychlé ověření můžeš spustit:
```bash
python cistic-prepisu.py
```

A sledovat výstup - měl bys vidět všechny indikátory výše.

## 💡 Tip

Pokud chceš vidět detailnější informace, můžeš v OpenRouter dashboardu:
1. Kliknout na konkrétní request
2. Zobrazit si celý payload (co bylo posláno)
3. Zobrazit si response (co přišlo zpět)
4. Zkontrolovat náklady

---

**Dulezite:** Pokud skript běží, ale v OpenRouter dashboardu nevidíš žádné requesty, znamená to, že se pravděpodobně používá něco jiného (nebo skript nefunguje správně).
