#Bucle while 

#Como un FOR
lista = [1,2,3,4]
contador = 0

while contador != len(lista):
    print(lista[contador])
    contador = contador + 1

for elemento in lista:
    print(elemento)
    
#Ejecutará las instrucciones que tenga dentro mientras no se cumpla la condición de guarda del bucle

contador = 0
while contador < 10:
    contador += 1
    print("Iteración", contador)

#While=True combinado con break nos permite un bucle infinito mientras no se cumpla la condición

while True:
    print("Introduzca un valor mayor que 5:")
    a = int(input())
    if a > 5:
        print("Es correcto")
        break
    else:
        print("Es incorrecto, pruebe de nuevo")




