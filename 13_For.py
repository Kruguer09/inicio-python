#Bucle For 

#Nos permite recorrer una lista o diccionario

nombres = ['María', 'Antonio', 'Gloria', 'Carmen']
for nombre in nombres:
    print(nombre)

#Para una lista de diccionarios, no lo hemos visto pero es muy útil

personas = []
a = {'nombre':'María', 'edad': 28}
b = {'nombre':'Gloria', 'edad': 35}

personas.append(a)
personas.append(b)

print(personas)

for persona in personas:
    print(persona['nombre'], persona['edad'])

#Nos permite acceder a los valores del diccionario y operar con ellos. Por ejemplo para crear una nueva lista

lista_nombres = []

for persona in personas:
    lista_nombres.append(persona['nombre'])
print(lista_nombres)

#Podemos coger una lista de números y modificar cada valores
"""
numeros = [1, 2, 3, 4, 5]

for index, numero in enumerate(numeros):
    numeros[index] += 3
print(numeros) """



