from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_pepito = Laptop("Lenovo", "i7", 32)
laptop_maria = Laptop("Lenovo", "i7", 32, 600)

# laptop_juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")
# print(laptop_juanito.realizar_diagnostico_sistema())

laptop_nachito = Laptop_Business("MSI", "i7", 4, 256, 8)
print(laptop_nachito.realizar_diagnostico_sistema())



# for numero in range(1,1000):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)
#print(Laptop.comparar_Costo(laptop_pepito, laptop_maria))
