# app.py
import streamlit as st
from Modulos.login import login
from Modulos.ahorro import mostrar_ahorro
# Primero ejecutamos el login
if login():
    # Si el login fue exitoso, mostramos el contenido de ahorro
    mostrar_ahorro()
else:
    st.warning("Acceso denegado. Por favor, inicia sesión correctamente.")
