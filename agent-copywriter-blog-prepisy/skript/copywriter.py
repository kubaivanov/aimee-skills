#!/usr/bin/env python3
"""
Agent pro tvorbu blogovych clanku z prepisu pres OpenRouter API.
Vytvori 3 varianty clanku najednou.
"""

import sys
import os
import requests
import re
import unicodedata
from pathlib import Path
from dotenv import load_dotenv

# Nacti .env soubor
load_dotenv()

# Cesty
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
INSTRUKCE_FILE = PROJECT_DIR / "AGENTS.md"
VYSTUP_DIR = PROJECT_DIR / "clanky-k-editaci"

# OpenRouter API
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Model pro psani (Opus nebo Gemini jsou nejlepsi na kreativitu)
MODELS = [
    "anthropic/claude-3.5-sonnet", # Skvela kreativita a styl
    "google/gemini-pro-1.5",       # Alternativa
]

def nacti_api_klic():
    """Nacte API klic z prostredi nebo souboru."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key:
        return api_key
    
    local_key_file = SCRIPT_DIR / ".api_key"
    if local_key_file.exists():
        with open(local_key_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
            
    raise ValueError("API klic nebyl nalezen. Nastavte promennou prostredi OPENROUTER_API_KEY nebo vytvorte soubor .api_key ve slozce skript/.")

def nacti_instrukce():
    """Nacte instrukce z AGENTS.md."""
    try:
        with open(INSTRUKCE_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Soubor s instrukcemi nebyl nalezen: {INSTRUKCE_FILE}")
        sys.exit(1)

def uloz_clanek(obsah, varianta):
    """Extrahuje nazev a ulozi clanek do souboru."""
    from datetime import datetime
    dnes = datetime.now().strftime("%Y-%m-%d")
    
    # Zkus najit nazev v textu (hleda prvni # nadpis nebo Nazev:)
    nazev_match = re.search(r'^#\s+(.*)$', obsah, re.MULTILINE)
    if not nazev_match:
        nazev_match = re.search(r'Nazev:\s*(.*)$', obsah, re.MULTILINE)
    
    titulek = nazev_match.group(1).strip() if nazev_match else f"clanek-{varianta}"
    
    # Ocisti nazev pro soubor
    file_name_base = titulek.lower().replace(" ", "-")
    # Odstran diakritiku
    file_name_base = "".join(c for c in unicodedata.normalize('NFD', file_name_base) if unicodedata.category(c) != 'Mn')
    # Odstran specialni znaky
    file_name_base = re.sub(r'[^a-z0-9-]', '', file_name_base)
    file_name_base = re.sub(r'-+', '-', file_name_base)
    
    file_path = VYSTUP_DIR / f"{dnes}-{varianta}-{file_name_base}.md"
    
    VYSTUP_DIR.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(obsah)
    
    return file_path

def generuj_clanky(text_prepisu, api_key, instrukce):
    """Posle prepis k vygenerovani clanku."""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/aibility",
        "X-Title": "Copywriter Agent"
    }
    
    print(f"🚀 Generuji 3 varianty clanku...", flush=True)
    
    # Pouzijeme jeden velky prompt pro vsechny varianty najednou podle AGENTS.md
    payload = {
        "model": MODELS[0],
        "messages": [
            {"role": "system", "content": instrukce},
            {"role": "user", "content": f"Zde je vycisteny prepis webinaru. Vytvor z nej prosim 3 varianty clanku (A, B, C) presne podle tvych instrukci:\n\n{text_prepisu}"}
        ],
        "temperature": 0.7,
    }
    
    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=300 # 5 minut
        )
        
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            
            # Rozdel obsah na jednotlive varianty (hleda Varianta A, B, C)
            varianty = {}
            parts = re.split(r'(?=Varianta [ABC])', content)
            
            for part in parts:
                if "Varianta A" in part: varianty['A'] = part.strip()
                elif "Varianta B" in part: varianty['B'] = part.strip()
                elif "Varianta C" in part: varianty['C'] = part.strip()
            
            if not varianty:
                print("⚠️ Nepodarilo se automaticky rozdelit varianty, ukladam vse do jednoho souboru.")
                return [uloz_clanek(content, "ALL")]
            
            ulozeno = []
            for var, text in varianty.items():
                cesta = uloz_clanek(text, var)
                ulozeno.append(cesta)
            return ulozeno
            
        else:
            print(f"❌ Chyba API: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Chyba: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Pouziti: python3 copywriter.py <vstupni_vycisteny_prepis>")
        sys.exit(1)
    
    vstup = Path(sys.argv[1])
    if not vstup.exists():
        print(f"❌ Vstupni soubor neexistuje: {vstup}")
        sys.exit(1)
        
    api_key = nacti_api_klic()
    instrukce = nacti_instrukce()
    
    with open(vstup, 'r', encoding='utf-8') as f:
        prepis = f.read()
    
    vysledky = generuj_clanky(prepis, api_key, instrukce)
    
    if vysledky:
        print("\n✅ Clanky byly uspesne vygenerovany a ulozeny:")
        for v in vysledky:
            print(f"   - {v.name}")
    else:
        print("\n❌ Generovani clanku selhalo.")

if __name__ == "__main__":
    main()
