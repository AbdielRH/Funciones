def ReotmarPromedio(v1, v2, v3):
    promedio = (v1 + v2  + v3) // 3
    return promedio
#Bloque Principal
valor1 = int(input("Ingresar el primer valor"))
valor2 = int(input("Ingrese el segundo valor"))
valor3 = int(input("Ingrese el tercer valor"))

print( "Valor promedio de los 3 numeros es " )
print(ReotmarPromedio(valor1, valor2, valor3))