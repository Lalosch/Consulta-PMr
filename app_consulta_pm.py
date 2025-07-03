
import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS1L2nRoYBYQPyZXJdhDk0xehT-8fPE1w8pI1T1lZOd84rqdZauUjVo3aEExKYKTD20TOJVvBiC_lza/pub?output=csv"
    df = pd.read_csv(url)
    df.columns = [col.strip() for col in df.columns]
    return df

df = cargar_datos()

st.title("Consulta tus PM 💰")
st.markdown("Ingresá tu nombre y contraseña para ver cuántas PM tenés.")
st.markdown("**(La contraseña es la que figura en el Excel)**")

nombre_input = st.text_input("Tu nombre (respetá mayúsculas/minúsculas):")
password_input = st.text_input("Contraseña:", type="password")

if st.button("Consultar"):
    user_row = df[df['Nombre'] == nombre_input]

    if not user_row.empty:
        password_real = user_row.iloc[0]['Contraseña']
        if password_input == password_real:
            pm = user_row.iloc[0]['PM Totales']
            st.success(f"Tenés {pm} PM 💸")
        else:
            st.error("Contraseña incorrecta.")
    else:
        st.error("Nombre no encontrado.")
import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS1L2nRoYBYQPyZXJdhDk0xehT-8fPE1w8pI1T1lZOd84rqdZauUjVo3aEExKYKTD20TOJVvBiC_lza/pub?gid=470759668&single=true&output=csv"
    df = pd.read_csv(url)
    df.columns = [col.strip() for col in df.columns]
    return df

df = cargar_datos()

st.title("Consulta tus PM 💰")
st.markdown("Ingresá tu nombre y contraseña para ver cuántas PM tenés.")
st.markdown("**(La contraseña es la que figura en el Excel)**")

nombre_input = st.text_input("Tu nombre (respetá mayúsculas/minúsculas):")
password_input = st.text_input("Contraseña:", type="password")

if st.button("Consultar"):
    user_row = df[df['Nombre'] == nombre_input]

    if not user_row.empty:
        password_real = user_row.iloc[0]['Contraseña']
        if password_input == password_real:
            pm = user_row.iloc[0]['PM Totales']
            st.success(f"Tenés {pm} PM 💸")
        else:
            st.error("Contraseña incorrecta.")
    else:
        st.error("Nombre no encontrado.")
