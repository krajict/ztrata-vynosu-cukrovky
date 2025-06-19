
# Kalkulačka ztráty výnosu cukrovky

Tato aplikace umožňuje odhadnout ztrátu výnosu cukrovky v závislosti na:
- datu zasetí,
- datu škodní události,
- míře poškození chrástu (%).

## Jak aplikace funguje
Po zadání vstupních údajů aplikace:
1. Spočítá počet dní mezi výsevem a škodou.
2. Podle interpolovaných dat určí ztrátu výnosu v %.
3. Zobrazí výsledek také graficky – včetně křivky, čárkovaných čar a popisků.

## Lokální spuštění

1. Ujistěte se, že máte nainstalovaný [Python](https://www.python.org/) (verze 3.8 nebo vyšší).
2. Nainstalujte potřebné balíčky:
```
pip install -r requirements.txt
```
3. Spusťte aplikaci:
```
streamlit run streamlit_ztrata_vynosu_cukrovky_2025_app_final.py
```

## Streamlit Cloud

1. Nahrajte následující soubory na [Streamlit Cloud](https://share.streamlit.io):
   - `streamlit_ztrata_vynosu_cukrovky_2025_app_final.py`
   - `requirements.txt`

2. Po nahrání bude aplikace automaticky spuštěna online.

---

📊 Vyvinuto pro podporu rozhodování při pojišťování a škodách v pěstování cukrovky.
