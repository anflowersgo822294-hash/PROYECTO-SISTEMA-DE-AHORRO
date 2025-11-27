import streamlit as st
from Modulos.login import login          # correcto: sigue siendo Modulos
from Modulos.ahorro import mostrar_ahorro

# Primero ejecutamos el login
if login():
    # Mostrar contenido según el tipo de usuario
    if st.session_state.get("tipo_usuario") == "Administrador":
        st.subheader("🔧 Panel de administración")
        # Aquí puedes agregar funciones exclusivas para administradores
    else:
        st.subheader("👤 Panel de usuario")
        # Aquí puedes agregar funciones para usuarios normales

    # Mostrar contenido común de ahorro
    mostrar_ahorro()
else:
    st.warning("Acceso denegado. Por favor, inicia sesión correctamente.")
