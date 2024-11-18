import random
ecuador = random.randint(10, 90)
colombia = random.randint(10, 100)
peru = random.randint(10, 120)

if ecuador >= 10 and ecuador <= 50:
    print("Buena velocidad en Zona Urbana de Ecuador")
elif ecuador >= 51 and ecuador <= 70:
    print("Buena velocidad en Zona Rural de Ecuador")
elif ecuador >= 71 and ecuador <= 90:
    print("Buena velocidad en Zona Perimetral de Ecuador")
else:
    print("Disminuye tu velocidad estas en Ecuador!!!")

if colombia >= 10 and colombia <= 30:
    print("Buena velocidad en Zona Urbana de Colombia")
elif colombia >= 31 and colombia <= 80:
    print("Buena velocidad en Zona Rural de Colombia")
elif colombia >= 81 and colombia <= 100:
    print("Buena velocidad en Zona Perimetral de Colombia")
else:
    print("Disminuye tu velocidad estas en Colombia!!!")

if peru >= 10 and peru <= 30:
    print("Buena velocidad en Zona Urbana de Peru")
elif peru >= 31 and peru <= 80:
    print("Buena velocidad en Zona Rural de Peru")
elif peru >= 81 and peru <= 100:
    print("Buena velocidad en Zona Perimetral de Peru")
else:
    print("Disminuye tu velocidad estas en Peru!!!")