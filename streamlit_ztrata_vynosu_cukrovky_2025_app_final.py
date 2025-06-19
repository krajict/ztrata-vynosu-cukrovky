
import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ztráta výnosu cukrovky", layout="centered")

st.title("Kalkulačka ztráty výnosu cukrovky")
st.write("Zadejte datum setí, datum škodní události a odhadované poškození chrástu v procentech.")

sowing_input = st.text_input("Datum setí (ve formátu DD. MM. RRRR)", value="01. 04. 2025")
damage_input = st.text_input("Datum škody (ve formátu DD. MM. RRRR)", value="01. 06. 2025")

def parse_cz_date(date_str):
    try:
        return datetime.datetime.strptime(date_str.strip(), "%d. %m. %Y").date()
    except:
        return None

sowing_date = parse_cz_date(sowing_input)
damage_date = parse_cz_date(damage_input)

if not sowing_date or not damage_date:
    st.error("Zadejte obě data ve správném formátu: DD. MM. RRRR (např. 01. 04. 2025).")
else:
    damage_percent = st.slider("Poškození chrástu (%)", min_value=10, max_value=100, step=10)
    days_after_sowing = (damage_date - sowing_date).days
    st.write(f"Počet dní od zasetí do škody: **{days_after_sowing} dní**")

    days = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    damage_levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    loss_data = [[0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 0, 0], [0, 2, 3, 5, 6, 8, 8, 7, 5, 4, 2, 2, 1, 0], [1, 3, 4, 6, 8, 10, 10, 9, 7, 5, 4, 3, 1, 0], [0, 2, 3, 4, 6, 8, 10, 10, 9, 7, 5, 3, 2, 0], [1, 4, 5, 7, 9, 11, 13, 13, 11, 10, 7, 4, 3, 0], [2, 5, 7, 9, 12, 15, 16, 16, 14, 12, 10, 5, 4, 1], [3, 7, 9, 12, 15, 18, 19, 20, 16, 15, 12, 7, 6, 2], [4, 9, 12, 16, 18, 21, 22, 24, 20, 19, 16, 10, 7, 3], [5, 11, 16, 20, 23, 25, 26, 28, 25, 23, 20, 14, 9, 4], [6, 13, 20, 24, 27, 30, 32, 33, 30, 28, 24, 18, 12, 6]]
    xticks = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

    df = pd.DataFrame(loss_data, index=damage_levels, columns=days)

    if days_after_sowing < 0:
        st.warning("Datum škody je dříve než datum setí.")
    elif days_after_sowing < min(days) or days_after_sowing > max(days):
        st.warning("Datum škody je mimo rozsah dostupných dat (20–150 dní po zasetí).")
    else:
        interpolated_loss = np.interp(days_after_sowing, days, df.loc[damage_percent])
        interpolated_loss = round(interpolated_loss, 1)
        st.success(f"Odhadovaná ztráta výnosu: **{interpolated_loss:.1f} %**")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(days, df.loc[damage_percent], label=f"{damage_percent}% poškození", color="tab:blue")
        ax.axvline(x=days_after_sowing, color='gray', linestyle='--')
        ax.axhline(y=interpolated_loss, color='gray', linestyle='--')
        ax.plot(days_after_sowing, interpolated_loss, 'ro')
        ax.set_xticks(xticks)
        ax.text(days_after_sowing + 1, 0, f"{days_after_sowing} dní", color='gray', verticalalignment='bottom')
        ax.text(min(days), interpolated_loss + 0.5, f"{interpolated_loss:.1f} %", color='gray')

        ax.set_title("Ztráta výnosu cukrovky")
        ax.set_xlabel("Počet dní od zasetí")
        ax.set_ylabel("Ztráta výnosu (%)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
