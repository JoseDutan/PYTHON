import random
aleatorio = random.randint(1, 9)
aleatorio_dos = random.randint(1, 9)

if aleatorio ==4:
    print("Te ganaste un chupete")
elif aleatorio == 8:
    print("Te ganaste un balon")
elif aleatorio == 3 and aleatorio_dos == 7:
    print("Te ganaste un Televisor")
else:
    print("Perdiste!!!")
    
    

import random
zona_Urbana = random.randint(10, 50)
zona_Rural = random.randint(31, 70)
zona_Perimetral = random.randint(71, 90)

if zona_Urbana == 10 and zona_Urbana == 50:
    print("Vas a una buena velocidad en Zona Urbana")
elif zona_Rural == 51 and zona_Rural == 70:
    print("Vas a una buena velocidad en Zona Rural")
elif zona_Perimetral == 71 and zona_Perimetral == 90:
    print("Vas a una buena velocidad en Zona Perimetral")
else:
    print("Te exediste de velocidad, disminuye tu velocidad!!!")