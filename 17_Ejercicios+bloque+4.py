#Ejercicios Funciones

#Crea un programa con una función que calcule el cuadrado de un valor dado (por teclado o directamente)

def cuadrado(a):
    return a * a

a = 5
resultado = cuadrado(a)
print(resultado)

#Un programa con una función que reciba una lista, la procese y nos devuelva una nueva lista con cada elemento multiplicado por dos

def multiplicar_lista(a):
    nuevaLista = []
    for numero in a:
        nuevaLista.append(numero * 2)
    """for index, numero in enumerate(numeros):
        numeros[index] *= 2"""
    return nuevaLista

numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_lista(numeros)
print(resultado)

#un programa que reciba dos números por teclado y los procese en una función y devuelva si son o no iguales

def validar_numeros(a,b):
    if a == b:
        return True
    else:
        return False
print("Introduzca un número")
a = int(input())
print("Introduzca otro número")
b = int(input())
resultado = validar_numeros(a,b)
if resultado:
    print("Son iguales")
else:
    print("Son distintos")
    

#Calculadora
def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

print("Introduce un número: ")
numero1 = int(input())
print("Introduce un número: ")
numero2 = int(input())

while True:
    print("MENÚ")
    print("Elija la opción para operar:\n1. Multiplicar.\n2. Dividir.\n3. Sumar.\n4. Restar.\n5. Salir.")
    opcion = input()
    if opcion == "1":
        res = multiplicar(numero1,numero2)
        print("La multiplicación es: ",res)
        break
    elif opcion == "2":
        res = dividir(numero1,numero2)
        print("La división es: ",res)
        break
    elif opcion == "3":
        res = sumar(numero1,numero2)
        print("La suma es: ",res)
        break
    elif opcion == "4":
        res = restar(numero1,numero2)
        print("La resta es: ",res)
        break
    elif opcion == "5":
        print("Cerrando la calculdora...")
        break
    else:
        print("Opción incorrecta.")