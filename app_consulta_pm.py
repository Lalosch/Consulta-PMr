
import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Consulta PM", page_icon="💰")

st.title("Consulta tus PM 💰")
st.markdown("Ingresá tu nombre y contraseña para ver cuántas PM tenés.")
st.markdown("**(La contraseña es tu nombre sin espacios + 'papu', todo en minúscula)**")

# --- CARGA DE DATOS DESDE GOOGLE SHEETS ---
@st.cache_data(ttl=300)
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-uF9T7oQnnVw1wCzq4pUJ8ZoUsj1PdkZTuUeUxqVaKft2kiyqiyMVRwK2SRknD1zAIP3KaJwJKhzF/pub?output=csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    return df

df = cargar_datos()

# --- FORMULARIO DE LOGIN ---
with st.form("login"):
    nombre_ingresado = st.text_input("Nombre").strip()
    password_ingresado = st.text_input("Contraseña", type="password")
    submit = st.form_submit_button("Consultar")

if submit:
    if nombre_ingresado == "":
        st.warning("Ingresá tu nombre.")
    else:
        nombre_normalizado = nombre_ingresado.replace(" ", "").lower()
        contraseña_esperada = nombre_normalizado + "papu"

        if password_ingresado.lower() != contraseña_esperada:
            st.error("Contraseña incorrecta.")
        else:
            # Buscar en la tabla
            fila = df[df["Nombre"].str.strip().str.lower() == nombre_ingresado.strip().lower()]
            if fila.empty:
                st.error("No se encontró tu nombre en la base de datos.")
            else:
                pm = fila.iloc[0]["PM Totales"]
                st.success(f"Tenés {pm} PM ✨")
