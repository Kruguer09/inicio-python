class Figura:
    
    def __init__(self, num_lados, longitud):
        self.num_lados = num_lados
        self.longitud = longitud
    
    def hallar_perimetro(self):
        return self.num_lados * self.longitud
        
piramide = Figura(4,8)
res = piramide.hallar_perimetro()


class Usuario:
    
    def __init__(self,nombre,pin,saldo):
        self.nombre = nombre
        self.pin = pin
        self.saldo = saldo
    
class Banco:
    
    def __init__(self,usuarios=[]):
        self.usuarios = usuarios
        
    def autenticar(self,nombre,pin):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.pin == pin:
                    print("Estás logueado")
                    return True
                else:
                    print("Pin incorrecto")
                    return False
        else:
            print("El usuario no existe")
            return False
            
    def sacar_dinero(self,nombre,saldo):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.saldo < saldo:
                    print("Saldo insuficiente")
                    break
                elif usuario.saldo >= saldo:
                    usuario.saldo -= saldo
                    print("El saldo disponible es ", usuario.saldo)
        
        
ana = Usuario('Ana', 9872, 450)
pablo = Usuario('Pablo', 5555, 200)
rodrigo = Usuario('Rodrigo', 2222, 900)

banco = Banco(usuarios=[ana,pablo,rodrigo])


while True:
    print('Bienvenido al banco. Por favor, idéntifiquese.')
    print('Introduzca el nombre')
    nombre = input()
    print('Introduzca el pin')
    pin = int(input())
    if banco.autenticar(nombre,pin):
        while True:
            print('Por favor, elija una de estas opciones.\n1. Sacar dinero\n2.Terminar sesión')
            opcion = input()
            if opcion == '1':
                print("Introduce cantidad a sacar")
                saldo = int(input())
                banco.sacar_dinero(nombre,saldo)
            elif opcion == '2':
                print("Saliendo del sistema")
                break
            else:
                print('Opción incorrecta. Por favor, introduzca otra opción')
    else:
        print("Usuario no autenticado, por favor, introduzca un nombre y pin correctos")
    
    
