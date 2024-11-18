import informacion

cantidad_voluntarios = int(input("Cuantos voluntarios desea ingresar: "))
for i in range(cantidad_voluntarios):
    info = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su año de Nacimiento: "))
    informacion.agregar_nombre(info)
    informacion.agregar_edad(edad)
informacion.paciente_min_max()