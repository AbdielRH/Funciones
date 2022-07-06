def largo (cadena):
    return len(cadena)

#BlooqUE Principal del programa


Nombre1 = input("Ingrese su nombre")
Nombre2 = input("Ingrese segundo nombre")
la1 = largo (Nombre1)
la2 = largo(Nombre2)
if la1 == la2:
    print("Los Nombres : ", Nombre1 ,"y", Nombre2 , "Tienes la misma catidad de caracteres")
else:
    if la1 > la2:
        print(Nombre1, "Es mas largo")
    else:
        print(Nombre2, " Es mar largo ")
