
import streamlit as st
import pandas as pd
import datetime
import numpy as np

st.set_page_config(page_title="Ztráta výnosu cukrovky", layout="centered")

st.title("Kalkulačka ztráty výnosu cukrovky")
st.write("Zadejte datum setí, datum škodní události a odhadované poškození chrástu v %.")

# Vstupy uživatele
sowing_date = st.date_input("Datum setí", value=datetime.date(2025, 4, 1))
damage_date = st.date_input("Datum škody", value=datetime.date(2025, 6, 1))
damage_percent = st.slider("Poškození chrástu (%)", min_value=10, max_value=100, step=10)

# Výpočet dnů od setí
days_after_sowing = (damage_date - sowing_date).days
st.write(f"Počet dní od zasetí do škody: **{days_after_sowing} dní**")

# Tabulka podle doložených hodnot
days = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
damage_levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
loss_data = [
    [0,  0,  1,  2,  3,  3,  2,  1,  1,  0,  0,  0],
    [0,  1,  2,  4,  5,  5,  4,  3,  2,  1,  0,  0],
    [1,  2,  4,  6,  7,  7,  8,  5,  3,  2,  1,  0],
    [3,  4,  6,  8, 10, 10,  9,  7,  5,  3,  2,  0],
    [5,  8,  8, 11, 13, 13, 11, 10,  7,  4,  3,  0],
    [7,  9, 11, 15, 16, 16, 14, 12, 10,  5,  4,  1],
    [9, 12, 15, 18, 19, 20, 16, 15, 12,  7,  6,  2],
    [12,16, 19, 21, 22, 24, 20, 19, 16, 10,  7,  3],
    [16,20, 23, 25, 26, 28, 25, 23, 20, 14,  9,  4],
    [20,24, 27, 30, 32, 33, 30, 28, 24, 18, 12,  6],
]
df = pd.DataFrame(loss_data, index=damage_levels, columns=days)

# Interpolace podle dnů a poškození
if days_after_sowing < 40 or days_after_sowing > 150:
    st.warning("Datum škody je mimo rozsah dostupných dat (40–150 dní po zasetí).")
else:
    interpolated_loss = np.interp(
        days_after_sowing,
        days,
        df.loc[damage_percent]
    )
    st.success(f"Odhadovaná ztráta výnosu: **{interpolated_loss:.1f} %**")
