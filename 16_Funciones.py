#Funciones

#Definición y llamada

def mostrar_texto():
    print('Hola')
    
mostrar_texto()

def multiplicar():
    a = 5
    b = 8
    print(a * b)

multiplicar()

#Ámbito de las variables. Las variables declaradas DENTRO de la función no son accesibles desde fuera, solo desde la propia función
#Las de fuera, sin embargo, sí son accesibles desde dentro de la función

def multiplicar():
    print(a * b)

a = 5
b = 8
multiplicar()

#Las funciones pueden devolver valores con la instrucción return
#En el siguiente caso devolvemos la multiplicación, y el resultado lo guardamos en una variable, que luego imprimimos sumándole un valor

def multiplicar():
    a = 5
    b = 8
    return a * b

resultado = multiplicar()
print(resultado + 5)

#Podemos devolver cualquier tipo de dato, y tratarlo como tal fuera de la función

def validar_dato():
    if a == 5:
        return True
    else:
        return False

a = 5
resultado = validar_dato()
print(resultado)

#El potencial de la función, es poder pasarle un dato para que opere con él, lo que se llama argumento.

def validar_dato(a, b):
    if a == b:
        return True
    else:
        return False

a = 5
b = 3
resultado = validar_dato(a,b)
print(resultado)

#Si lo combinamos con un bucle for, nos queda un código mucho más sencillo que si lo hiciéramos contemplando cada caso.
#En este caso, recorremos una lista de números y vemos si el valor introducido por pantalla existe en la lista.

def validar_dato(a):
    if a == b:
        return True
    else:
        return False

numeros = [1, 2, 3, 4, 5, 6]
print("Introduce un número para ver si está en la lista")
b = int(input())

for numero in numeros:
    if validar_dato(numero):
        print("El número",b,"está en la lista")
        break
else: #este else está fuera del if, realmente no es muy recomendable, pero podría usarse así.
    print("El número",b,"no está en la lista")
    


