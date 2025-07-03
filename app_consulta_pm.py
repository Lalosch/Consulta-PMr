
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Consulta tus PM", page_icon="💰")

st.title("Consulta tus PM 💰")
st.markdown("Ingresá tu **contraseña** para ver cuántas PM tenés.")

@st.cache_data
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS1L2nRoYBYQPyZXJdhDk0xehT-8fPE1w8pI1T1lZOd84rqdZauUjVo3aEExKYKTD20TOJVvBiC_lza/pub?output=csv"
    df = pd.read_csv(url)
    df.columns = [col.strip().lower() for col in df.columns]
    return df

df = cargar_datos()

# Pide contraseña
password_input = st.text_input("Contraseña:", type="password")

if st.button("Consultar"):
    user_row = df[df['contraseña'] == password_input]
    if not user_row.empty:
        nombre = user_row.iloc[0]['nombre']
        pm = user_row.iloc[0]['pm totales']
        st.success(f"{nombre}, tenés {pm} PM 💸")
    else:
        st.error("Contraseña incorrecta.")
