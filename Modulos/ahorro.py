# ahorro.py

from datetime import datetime

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

# Simulación de uso
if __name__ == "__main__":
    ahorro1 = Ahorro(id_ahorro=1, id_miembro=101, id_reunion=5, monto=25.0, otras_actividades=5.0)
    print("📌 Registro de Ahorro:")
    for clave, valor in ahorro1.resumen().items():
        print(f"{clave}: {valor}")
