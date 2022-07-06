def retomar_mayor (v1 , v2):
    if v1 > v2 :
        mayor = v1
    else:
        mayor = v2
    return mayor
#blouqe Principal

valor1 = int(input("ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor : "))
print("El numero mayor es :", retomar_mayor(valor1 , valor2))
