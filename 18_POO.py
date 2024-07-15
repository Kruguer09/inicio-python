#Programación orientada a objetos

#Los objetos están formados de su constructor, su definición y sus métodos. Vamos a verlo con el ejemplo de coche

class Coche: #Definimos la clase coche
    pass #No hace nada

coche = Coche() #Creamos un objeto de la clase coche
coche.color = "verde" #Damos valor a dos atributos del objeto coche (color y motor)
coche.motor = "gasolina"

print("Mi coche es de color", coche.color, "y de motor",coche.motor)

#En el ejemplo vemos que definimos la clase Coche, lo instanciamos y le damos valor a dos de sus atributos

#Existe la posibilidad de inicializar atributos de la clase con un valor por defecto a la hora de crearlos.

class Coche:
    marca = "Ford"
    
coche = Coche()
print(coche.marca)

#Esto nos hace más fácil la instanciación de objetos y nos permite darle un valor por defecto a algún atributo, aunque siempre puede cambiarse como hemos visto arriba.

#Aparte de atributos, existen los métodos de clase, los cuales llevan SIEMPRE el argumento self (haciendo referencia a la propia clase)

class Coche:
    pass

    def acelerar(self):
        print("Estoy acelerando el coche")

coche = Coche()
coche.acelerar()

#Si intentase llamar al método acelerar sin hacer referencia al objeto, dará error ya que es propio de la clase Coche.

#Por defecto, cualquier clase lleva incluído el método constructor, el cual crea el objeto. 
#Como vemos en la línea de coche = Coche(), esto crea un objeto y ya. El método constructor se puede sobreescribir para añadir funcionalidad
#En este ejemplo vamos a crear los objetos inicializándolos.

class Coche:
    pass
    
    def __init__(self, color, motor):
        self.color = color
        self.motor = motor
        
#Esto hará que cuando cree un objeto y le pase dos parámetros, ese objeto se cree con sus atributos color y motor rellenados

coche = Coche("verde", "gasolina")
print(coche.color, coche.motor)

#Aparte del constructor, también tiene el tipo String, que nos dice el texto que utilizará al hacerle un print al objeto (por defecto, la dirección de memoria del propio objeto)

class Coche:
    pass
    
    def __str__(self):
        return ("Soy un coche")
        
coche = Coche()
print(coche)

#Vamos a ponerlo en práctica con un ejercicio que disponga de la clase coche y de la clase concesionario, con sus métodos de clase

class Coche:

    def __init__(self, marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor
    
    def __str__(self):
        return print(self.marca,self.color)

class Concesionario:

    def __init__(self, coches=[]):
        self.coches = coches

    def mostrar_coche(self):
        for coche in self.coches:
            print(coche.marca, coche.color)

ford = Coche("ford", "rojo", "diesel")
mustang = Coche("mustang", "amarillo", "gasolina")

concesionario = Concesionario(coches=[ford, mustang])

concesionario.mostrar_coche()
