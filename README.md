# 📂 Aibility Content GitHub Repository

Tento repozitář slouží jako centrální úložiště pro správu obsahu, AI agentů a vzdělávacích materiálů projektu Aibility.

---

## 🏗️ Struktura složek

### 🤖 [agents/](./agents)
Obsahuje specializované AI agenty a automatizační nástroje.
- **agent-cistic-prepisu**: Nástroj pro čištění a formátování surových přepisů z webinářů.
- **agent-copywriter-blog-prepisy**: Generátor blogových článků (3 varianty) z vyčištěných textů.
- **framer-to-blog-agent**: Plně automatizované nasazování článků do Framer CMS včetně generování AI ilustrací.
*(Více detailů najdete v [README složky agents](./agents/README.md))*

### 🧠 [aimee-skills-description/](./aimee-skills-description)
Dokumentace a podklady pro schopnosti (skills) AI asistentky Aimee.
- Obsahuje složky pro jednotlivé dovednosti (např. *druhy-mozek*, *zaklady-promptovani*).
- Každá složka obsahuje vizuální podklady (`image.png`) a textový popis (`popis.md`).

### 📝 [prepisy-webinaru-edu/](./prepisy-webinaru-edu)
Úložiště pro surové i zpracované přepisy vzdělávacích webinářů.
- Slouží jako zdrojová data pro agenty v sekci `agents/`.
- Obsahuje soubory ve formátech `.docx` (původní) a `.md` (převedené pro další zpracování).

---

## 🛠️ Jak pracovat s tímto repozitářem
1. **Přepisy**: Nové přepisy vkládejte do `prepisy-webinaru-edu/`.
2. **Automatizace**: Pro zpracování obsahu používejte nástroje ve složce `agents/`.
3. **Dokumentace**: Schopnosti Aimee aktualizujte v `aimee-skills-description/`.

---

## 🔑 Důležité upozornění
Většina agentů vyžaduje vlastní konfiguraci v souborech `.env`. Tyto soubory jsou ignorovány Gitem pro zachování bezpečnosti API klíčů. Při prvním použití nástroje postupujte podle `README.md` v dané složce.
