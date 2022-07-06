#Elabora una funcion que nos retome el perimetro de un cuadrado pasado como parametro el valor de un lado
def Cuadrado(a):
    return a*4

#BoquePrincipal

a = int(input("Ingrese el lado del cuadro"))
Lado = Cuadrado(a)
print("El perimetro es ", Lado)
