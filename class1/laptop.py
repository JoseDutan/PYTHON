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


laptop_pepito = Laptop("Lenovo", "i7", 32)
print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final())
print(f"El valos del descuento: {laptop_pepito.valor_descuento(10)}")