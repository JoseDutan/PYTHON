menu = ["1. Añadir plato al menú.", "2. Buscar en el menú.", "3. Eliminar plato del menú", "4. Mostrar platos del menú"]
print(menu)
menu.insert(4, "5. Plato ingresado")
print(f"Plato encontrado: {menu.index("2. Buscar en el menú.")}")
menu.pop(3)
print(menu)