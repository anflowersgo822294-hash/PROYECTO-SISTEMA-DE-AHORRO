import streamlit as st
from Modulos.config.conexion import obtener_conexion

# Función para verificar credenciales en la tabla Socias
def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        # Consulta adaptada a tu tabla y columnas
        query = "SELECT Usuario FROM Socias WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        st.error(f"Error al verificar usuario: {e}")
        return None
    finally:
        con.close()

# Función de login con Streamlit
def login():
    st.title("🔑 Inicio de sesión")

    # Si ya hay sesión iniciada, mostrar mensaje
    if st.session_state.get("sesion_iniciada"):
        st.success(f"Bienvenida {st.session_state['usuario']} 👋")
        return True

    # Mostrar mensaje si la conexión fue exitosa antes
    if st.session_state.get("conexion_exitosa"):
        st.info("✅ Conexión a la base de datos establecida correctamente.")

    # Campos de entrada
    usuario = st.text_input("Usuario", key="usuario_input")
    contrasena = st.text_input("Contraseña", type="password", key="contrasena_input")

    # Botón de inicio de sesión
    if st.button("Iniciar sesión"):
        resultado = verificar_usuario(usuario, contrasena)
        if resultado:
            st.session_state["usuario"] = usuario
            st.session_state["sesion_iniciada"] = True
            st.success(f"Bienvenida {usuario} 👋")
            return True
        else:
            st.error("❌ Credenciales incorrectas.")
            return False

    return False
