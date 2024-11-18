class auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        print(f"{self.marca}, {self.modelo}, {self.año}")
    
    def actualizar_kilometraje(self, kilometraje):
        if kilometraje > self.kilometraje:
             self.kilometraje = kilometraje
             print(f"El kilometraje ha sido actualizado a {self.kilometraje} km.")
        else:
            print("No se puede reducir el Kilometraje")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Has recorrido {kilometros} km. Kilometraje total: {self.kilometraje} km.")
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo.")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado.")
        else:
            print("¡Ya déjame descansar por favor!")


mi_auto = auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_informacion()
mi_auto.actualizar_kilometraje(15000)
mi_auto.realizar_viaje(6000)
mi_auto.estado_auto()