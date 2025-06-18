
# Kalkulačka ztráty výnosu cukrovky

Tato aplikace slouží k odhadu ztráty výnosu cukrovky v závislosti na:
- datu setí,
- datu škodní události,
- a míře poškození chrástu (%).

Založeno na tabulkových datech z experimentálních výsledků, interpolováno pro libovolný den mezi 40. a 150. dnem po zasetí.

## ✅ Funkce
- Zadávání dat ve formátu **DD. MM. RRRR** (např. `01. 04. 2025`)
- Výběr poškození chrástu v rozsahu 10–100 %
- Výpočet počtu dní od zasetí
- Automatická interpolace ztráty výnosu (s ořezáním záporných hodnot)

## 📦 Jak spustit

1. Ujisti se, že máš nainstalovaný `streamlit`:
```bash
pip install streamlit
```

2. Spusť aplikaci:
```bash
streamlit run streamlit_ztrata_vynosu_cukrovky_cz_dd.mm.rrrr.py
```

3. Aplikace se otevře v prohlížeči na adrese `http://localhost:8501`

## 🌐 Nasazení online
Aplikaci lze jednoduše nasadit na [Streamlit Cloud](https://streamlit.io/cloud):

1. Vytvoř si účet a připoj GitHub
2. Vytvoř nový repozitář (např. `cukrovka-ztraty`)
3. Nahraj soubor `streamlit_ztrata_vynosu_cukrovky_cz_dd.mm.rrrr.py` a tento `README.md`
4. Na stránce Streamlit Cloud zvol „New app“, vyber repozitář a soubor
