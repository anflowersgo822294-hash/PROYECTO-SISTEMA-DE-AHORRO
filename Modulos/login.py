import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT Tipo_usuario FROM USUARIO WHERE usuario = %s AND contrasena = %s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        st.error(f"Error al verificar usuario: {e}")
        return None
    finally:
        con.close()

def login():
    st.title("🔑 Inicio de sesión")

    # Si ya hay sesión iniciada, mostrar mensaje y no repetir formulario
    if st.session_state.get("sesion_iniciada"):
        st.success(f"Bienvenido {st.session_state['usuario']} ({st.session_state['tipo_usuario']}) 👋")
        return True

    # Mostrar mensaje persistente si ya hubo conexión exitosa
    if st.session_state.get("conexion_exitosa"):
        st.info("✅ Conexión a la base de datos establecida correctamente.")

    usuario = st.text_input("Usuario", key="usuario_input")
    contrasena = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(usuario, contrasena)
        if tipo:
            st.session_state["usuario"] = usuario
            st.session_state["tipo_usuario"] = tipo
            st.session_state["sesion_iniciada"] = True
            st.success(f"Bienvenido {usuario} ({tipo}) 👋")
            return True
        else:
            st.error("❌ Credenciales incorrectas.")
            return False

    return False
