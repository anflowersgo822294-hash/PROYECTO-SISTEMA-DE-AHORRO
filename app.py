import streamlit as st
from Modulos.login import login          # correcto: sigue siendo Modulos
from Modulos.ahorro import mostrar_ahorro

def main():
    # Primero ejecutamos el login
    if login():
        # Mostrar contenido según el tipo de usuario
        tipo_usuario = st.session_state.get("tipo_usuario", "Usuario")  # valor por defecto

        if tipo_usuario == "Administrador":
            st.subheader("🔧 Panel de administración")
            # Aquí puedes agregar funciones exclusivas para administradores
            st.info("Opciones avanzadas disponibles solo para administradores.")
        else:
            st.subheader("👤 Panel de usuario")
            # Aquí puedes agregar funciones para usuarios normales
            st.info("Opciones disponibles para usuarios registrados.")

        # Mostrar contenido común de ahorro
        mostrar_ahorro()
    else:
        st.warning("Acceso denegado. Por favor, inicia sesión correctamente.")

if __name__ == "__main__":
    main()
