import streamlit as st
from datetime import datetime

def mostrar_ahorro():
    st.write("Bienvenido al sistema de ahorro")

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
