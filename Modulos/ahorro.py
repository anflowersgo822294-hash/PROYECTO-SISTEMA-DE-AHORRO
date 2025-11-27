import streamlit as st
from datetime import datetime

def mostrar_ahorro():
    st.title("💰 Sistema de ahorro")

    # Formulario para ingresar datos de ahorro
    id_ahorro = st.text_input("ID Ahorro")
    id_miembro = st.text_input("ID Miembro")
    id_reunion = st.text_input("ID Reunión")
    monto = st.number_input("Monto de ahorro", min_value=0.0, step=0.01)
    otras_actividades = st.number_input("Otros ingresos", min_value=0.0, step=0.01)

    if st.button("Registrar ahorro"):
        ahorro = Ahorro(id_ahorro, id_miembro, id_reunion, monto, otras_actividades)
        st.success("✅ Ahorro registrado correctamente")
        st.write("### 📊 Resumen del ahorro")
        st.json(ahorro.resumen())

class Ahorro:
    def __init__(self, id_ahorro, id_miembro, id_reunion, monto, otras_actividades=0.0):
        self.id_ahorro = id_ahorro
        self.id_miembro = id_miembro
        self.id_reunion = id_reunion
        self.monto = monto
        self.otras_actividades = otras_actividades
        self.fecha_registro = datetime.now()
        self.saldo_total = self.calcular_saldo()

    def calcular_saldo(self):
        return round(self.monto + self.otras_actividades, 2)

    def resumen(self):
        return {
            "ID Ahorro": self.id_ahorro,
            "Miembro": self.id_miembro,
            "Reunión": self.id_reunion,
            "Monto Ahorro": self.monto,
            "Otros Ingresos": self.otras_actividades,
            "Saldo Total": self.saldo_total,
            "Fecha": self.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    mostrar_ahorro()
