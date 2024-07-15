#Lectura por teclado

a = input()
print(a)

#Podemos operar con lo introducido por teclado (lo trata como texto, no como número)
#En el ejemplo introducimos una cadena de texto primero y luego un número

a = input()
print(a * 2)

#Lo mismo para caracteres
#En el ejemplo introducimos una letra

a = input()
print(a * 2)

#Si quisiéramos convertir lo introducido por teclado a entero, usaríamos int(cadena_por_teclado) para transformar cadena_por_teclado a entero

a = input()
b = int(a)
print(b * 2)