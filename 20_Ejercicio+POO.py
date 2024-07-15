#Ejercicios POO

#Crea un programa con las clases "librería" y "libro". Tendremos que poder consultar los libros de la libería, y vender libros (utiliza del para borrar un objeto)
#Muestra en un listado todos los libros de la librería, vende uno y vuelve a mostrar el listado

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return print(self.titulo, self.autor)

class Libreria:

    def __init__(self, libros):
        self.libros = libros

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.titulo)

    def vender_libro(self, titulo):
        librosNuevos = []
        
# for index, libro in enumerate(self.libros):
#            if libro.titulo == titulo:
#                del(self.libros[index])
#                print(libro.titulo, "vendido")"""
        
        for libro in self.libros:
            if libro.titulo != titulo:
                librosNuevos.append(libro)
        
        self.libros = librosNuevos
                
libro1 = Libro("Los pilares de la tierra", "Ken Follet")
libro2 = Libro("La sombra del viento", "Carlos Ruiz Zafón")

libreria = Libreria(libros=[libro1, libro2])
libreria.mostrar_libros()
libreria.vender_libro("Los pilares de la tierra")
libreria.mostrar_libros()

