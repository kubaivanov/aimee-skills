#!/usr/bin/env python3
"""
Jednoduchy skript pro vycisteni prepisu pres OpenRouter API.
Pouziti: python3 cistic-prepisu.py <vstupni_soubor> <vystupni_soubor>
"""

import sys
import os
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

# Nacti .env soubor pokud existuje
load_dotenv()

# Cesty
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
INSTRUKCE_FILE = PROJECT_DIR / "AGENTS.md"

# OpenRouter API
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Modely - Gemini je rychlejsi, Opus jako fallback
MODELS = [
    "google/gemini-3-pro-preview",  # Rychlejsi
    "anthropic/claude-opus-4.5",    # Fallback
]

# Max velikost casti (znaku) - ~20k tokenu
MAX_CHUNK_SIZE = 80000

# Kolik casti zpracovat paralelne
MAX_PARALELNICH = 5


def nacti_api_klic():
    """Nacte API klic z prostredi nebo souboru."""
    # 1. Zkus environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key:
        return api_key
    
    # 2. Zkus lokalni soubor .api_key
    local_key_file = SCRIPT_DIR / ".api_key"
    if local_key_file.exists():
        with open(local_key_file, 'r', encoding='utf-8') as f:
            return f.read().strip()

    raise ValueError("API klic nebyl nalezen. Nastavte promennou prostredi OPENROUTER_API_KEY nebo vytvorte soubor .api_key ve slozce skript/.")


def nacti_instrukce():
    """Nacte instrukce z AGENTS.md - jen sekci pravidel."""
    try:
        with open(INSTRUKCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        # Vrat jen relevantni cast
        if "## 🎯 Pravidla pro cisteni" in content:
            start = content.find("## 🎯 Pravidla pro cisteni")
            end = content.find("## 📁 Cesty", start)
            if end > start:
                return content[start:end]
        return content
    except FileNotFoundError:
        return None


def rozdel_na_casti(text, max_size=MAX_CHUNK_SIZE):
    """Rozdeli text na casti podle odstavcu."""
    if len(text) <= max_size:
        return [text]
    
    casti = []
    aktualni = ""
    
    for odstavec in text.split('\n\n'):
        if len(aktualni) + len(odstavec) + 2 <= max_size:
            aktualni += odstavec + '\n\n'
        else:
            if aktualni:
                casti.append(aktualni.strip())
            aktualni = odstavec + '\n\n'
    
    if aktualni:
        casti.append(aktualni.strip())
    
    return casti


def vycisti_text(text, api_key, instrukce, cast_info="", cast_index=0):
    """Posle text pres OpenRouter API k vycisteni."""
    
    system_prompt = """Jsi specializovany agent pro vycisteni prepisu webinaru.

TVUJ UKOL:
- Odstran casove znacky ([00:42], [01:15:30])
- Odstran organizacni poznamky (piste do chatu, zaznam posleme)
- Odstran vyplnova slova (eh, hm, no, proste, jakoby) - jen pokud nenese vyznam
- Oprav preklepy a neukoncene vety
- Rozdel do logickych odstavcu

CO ZACHOVAT:
- Veskery obsahovy obsah
- Myslenky, priklady, analogie
- Dotazy a odpovedi
- Jmena mluvcu

NIKDY text nezkracuj ani neshrnuj! Vystupem musi byt kompletni vycisteny prepis."""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/aibility",
        "X-Title": "Cistec prepisu"
    }
    
    user_content = text
    if cast_info:
        user_content = f"{cast_info}\n\n{text}"
    
    # Zkus kazdy model
    for model in MODELS:
        print(f"   [{cast_index}] 🌐 {model}...", end=" ", flush=True)
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            "temperature": 0.3,
        }
        
        try:
            response = requests.post(
                OPENROUTER_API_URL,
                headers=headers,
                json=payload,
                timeout=180  # 3 minuty
            )
            
            if response.status_code == 200:
                result = response.json()
                tokens = result.get('usage', {}).get('total_tokens', '?')
                print(f"✅ ({tokens} tokenu)", flush=True)
                return (cast_index, result['choices'][0]['message']['content'])
            
            print(f"⚠️ nedostupny", flush=True)
            
        except requests.exceptions.Timeout:
            print(f"⏱️ timeout", flush=True)
        except Exception as e:
            print(f"❌ {e}", flush=True)
    
    return (cast_index, None)


def main():
    if len(sys.argv) != 3:
        print("Pouziti: python3 cistic-prepisu.py <vstupni_soubor> <vystupni_soubor>")
        sys.exit(1)
    
    vstup = Path(sys.argv[1])
    vystup = Path(sys.argv[2])
    
    print(f"🧹 Cistic prepisu", flush=True)
    print(f"   Vstup:  {vstup.name}", flush=True)
    print(f"   Vystup: {vystup.name}", flush=True)
    
    # API klic
    try:
        api_key = nacti_api_klic()
    except Exception as e:
        print(f"❌ API klic: {e}")
        sys.exit(1)
    
    # Instrukce
    instrukce = nacti_instrukce()
    
    # Vstupni soubor
    try:
        with open(vstup, 'r', encoding='utf-8') as f:
            obsah = f.read()
    except Exception as e:
        print(f"❌ Cteni: {e}")
        sys.exit(1)
    
    print(f"   Velikost: {len(obsah):,} znaku", flush=True)
    
    if not obsah.strip():
        print("⚠️ Prazdny soubor")
        sys.exit(1)
    
    # Rozdel na casti
    casti = rozdel_na_casti(obsah)
    print(f"   Casti: {len(casti)}", flush=True)
    
    if len(casti) == 1:
        # Jedna cast - zpracuj normalne
        print(f"\n📝 Zpracovavam...", flush=True)
        vysledek = vycisti_text(casti[0], api_key, instrukce, "", 1)
        if vysledek[1] is None:
            print(f"❌ Nepodarilo se vycistit")
            sys.exit(1)
        vysledky = [vysledek[1]]
    else:
        # Vice casti - paralelni zpracovani
        print(f"\n🚀 Paralelni zpracovani (max {MAX_PARALELNICH} soucasne)...", flush=True)
        
        vysledky_dict = {}
        
        with ThreadPoolExecutor(max_workers=MAX_PARALELNICH) as executor:
            # Spust vsechny ulohy
            futures = {}
            for i, cast in enumerate(casti, 1):
                cast_info = f"Cast {i}/{len(casti)}"
                future = executor.submit(vycisti_text, cast, api_key, instrukce, cast_info, i)
                futures[future] = i
            
            # Počkej na výsledky
            for future in as_completed(futures):
                cast_index, vysledek = future.result()
                if vysledek is None:
                    print(f"\n❌ Cast {cast_index} selhala")
                    sys.exit(1)
                vysledky_dict[cast_index] = vysledek
        
        # Serad podle indexu
        vysledky = [vysledky_dict[i] for i in sorted(vysledky_dict.keys())]
    
    # Spoj a uloz
    finalni = "\n\n".join(vysledky)
    
    try:
        vystup.parent.mkdir(parents=True, exist_ok=True)
        with open(vystup, 'w', encoding='utf-8') as f:
            f.write(finalni)
        print(f"\n✅ Ulozeno: {vystup.name}", flush=True)
    except Exception as e:
        print(f"❌ Ukladani: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
