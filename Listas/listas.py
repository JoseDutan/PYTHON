#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Neptuno"]
# print(planetas[-3])
# print(planetas[2:8])
# print(len(planetas))
# print(planetas[8])

#TRABAJR CON UNA LISTA DE NUMEROS
gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 124054 #Newtons, en la Tierra

print(f"En la Tierra un autobus de dos pisos pes {peso_bus} N")
print(f"En Mercurio un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas[0]} N")

print(f"lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedad_en_planetas)}N")
print(f"Lo mas pesado que seria u autobus en sistema solar es {peso_bus * max(gravedad_en_planetas)} N")