import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        diagnostico_empresarial = {
            "ALMACENAMIENTO": "OK" if self.almacenamiento >= 256 else "Espacio insuficiente, actualizar almacenamiento",
            "DURACIÓN BATERÍA": "OK" if self.duracion_bateria >= 6 else "Batería no adecuada para uso empresarial"
        }
        resultado_diagnostico.update(diagnostico_empresarial)
        simulacion = self.verificar_conectividad()
        resultado_diagnostico["Resultado Conectividad"] = simulacion
        return resultado_diagnostico
    
    def verificar_conectividad(self):
        conectividad_red = {
            "Wi-Fi DISPONIBLE": random.choice([True, False]),
            "ACCESO A SERVIDORES EMPRESARIALES": random.choice([True, False]),
            "LATENCIA DE RED": "BAJA" if random.choice([True, False]) else "ALTA"
        }
        return conectividad_red
    
