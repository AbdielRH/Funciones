def cantidad_Palabra (Palabra):
    cant = 0
    for i in range(len(Palabra)):
        if(Palabra[i] == "a" ) or (Palabra[i] == "A"):
            cant +=1
            return cant

Letras = input("Ingresar una palabra")
print("La palabra", Letras, "tiene" , cantidad_Palabra(Letras), "letras a")
