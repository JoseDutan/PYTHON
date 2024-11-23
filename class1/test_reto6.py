from reto6 import auto
mi_auto1 = auto("Toyota", "Corolla", 2024)
mi_auto2 = auto("Toyota", "Corolla", 2024, 1000)
print(auto.comparar_kilometraje(mi_auto1, mi_auto2))

mi_auto3 = auto.toyota_auto("Hilux")
mi_auto3.mostrar_informacion()

auto_generico = auto.auto_generico()
auto_generico.mostrar_informacion()

print(auto.es_kilometraje_valido(-50))

