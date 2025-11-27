# app.py
import streamlit as st
from modulos.login import login
from modulos.ahorro import mostrar_ahorro  # Importamos la función mostrar_ahorro del módulo ahorro

# Primero ejecutamos el login
if login():
    # Si el login fue exitoso, mostramos el contenido de ahorro
    mostrar_ahorro()
else:
    st.warning("Acceso denegado. Por favor, inicia sesión correctamente.")
