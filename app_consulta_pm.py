
import streamlit as st
import pandas as pd
import hashlib

# Datos del Google Sheets
SHEET_ID = "1r-0hQcH7zmErPxfbQkUjqn3jR8BVSdPHREtheDK21_k"
SHEET_NAME = "PM"

@st.cache_data
def cargar_datos():
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    df["Nombre_norm"] = df["Nombre"].str.strip().str.lower()
    return df

def verificar(nombre, contraseña, df):
    nombre_norm = nombre.strip().lower()
    df_user = df[df["Nombre_norm"] == nombre_norm]
    if df_user.empty:
        return None
    h_esperado = df_user.iloc[0]["Password_hash"]
    h_ingresado = hashlib.sha256((nombre_norm + "papu").encode()).hexdigest()
    return df_user.iloc[0]["Total"] if h_ingresado == h_esperado else None

# Interfaz Streamlit
st.set_page_config(page_title="Consulta PM", page_icon="📊")
st.title("Consulta tus PM")

df = cargar_datos()
nombre = st.text_input("Nombre")
contraseña = st.text_input("Contraseña", type="password")

if st.button("Consultar"):
    pm = verificar(nombre, contraseña, df)
    if pm is not None:
        st.success(f"Hola {nombre.strip().capitalize()}, tenés {pm} PM.")
    else:
        st.error("Nombre o contraseña incorrectos.")
