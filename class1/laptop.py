import random
class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuestos = 10):
        self.marca = marca
        self.procesador = procesador
        self.memeoria = memoria
        self.costo = costo
        self.impuestos = impuestos

    def valor_final(self):
        return self.costo + self.impuestos

    def valor_descuento(self, descuento):
        return (self.costo *  descuento)/100
    
    def realizar_diagnostico_sistema(self):
        resulatdo = {
            "MARCA" : f"{self.marca}",
            "PROCESADOR" : f"{self.procesador}",
            "MEMORIA RAM" : "OK" if self.memeoria >= 8 else "Aumentar Memoria RAM",
            "BATERIA" : "OK" if random.choice([True, False]) else "Cambiar de bateria"
        }
        return resulatdo
 
    def realizar_informe_uso(self):
        resultado_informe = {
            "Tipo" : "Generica",
            "Uso Recomendado" : "Tareas cotidianas",
            "Horas de Uso" : 5,
            "Diagrama actual" : self.realizar_diagnostico_sistema()
        }
        return resultado_informe
    
    @staticmethod
    def comparar_Costo(Laptop1, Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    @classmethod
    def asus_laptop(clc, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return clc(marca, procesador, memoria, costo)