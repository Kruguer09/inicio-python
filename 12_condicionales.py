#Condicionales if/else

#Depende de la condición del IF, tomará un camino u otro

a = 2
if a == 2:
    print("a vale 2")
else:
    print("a es distinto de 2")
    
#Podemos concatenar condiciones con los operadores lógicos and, or y not

nombre = "María"
edad = 28

if nombre == "María" and edad == 28:
    print("Su nombre es María y tiene 28 años")
elif nombre == "María" and not edad == 28:
    print("Su nombre es María y no tiene 28 años")
elif nombre != "María" and edad == 28:      
    print("Su nombre no es María y tiene 28 años")
else:
    print("No se llama María ni tiene 28 años")

