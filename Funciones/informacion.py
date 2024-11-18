nombre_paciente = []
edad = []

def agregar_nombre(nombres):
    nombre_paciente.append(nombres)

#-----------------------------------------------------------------------
  
def agregar_edad(año_nacimiento):
    año_actual = 2024
    edad_actual = (año_actual - año_nacimiento )
    edad.append(edad_actual)
    print(f"Los pacientes agregados: {nombre_paciente}, {edad}")


#-----------------------------------------------------------------------

def paciente_min_max():
    if not edad:
        print("No hay pacientes registrados.")
        return
    
    max_edad = max(edad)
    min_edad = min(edad)
    paciente_mayor = nombre_paciente[edad.index(max_edad)]
    paciente_menor = nombre_paciente[edad.index(min_edad)]
    print(f"El paciente mayor es {paciente_mayor} con {max_edad} años.")
    print(f"El paciente menor es {paciente_menor} con {min_edad} años.")
