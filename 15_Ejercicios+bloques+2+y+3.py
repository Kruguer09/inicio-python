#BLOQUE II
#Crea un diccionario de libros con el título y año y recorre sus títulos con un bucle for

libros = {'Los pilares de la Tierra':'1989','El Codigo Da Vinci':'2003'}


for titulo in libros:
    print(titulo)
    
#Para el ejemplo anterior, recorre los años

for key in libros:
    print(libros[key])

#Lo mismo, pero mostrando tanto la clave como el valor

for key in libros:
    print(key, libros[key])
    


#Crea una lista de películas con el título, año y director, y muestra por pantalla los datos de la 3a posición

peliculas = []

a = {'titulo':'Star wars','año':'1977','director':'George Lucas'}
b = {'titulo':'El señor de los anillos','año':'2001','director':'Peter Jackson'}
c = {'titulo':'Psicosis','año':'1960','director':'Alfred Hitchcock'}

peliculas.append(a)
peliculas.append(b)
peliculas.append(c)

contador = 0
for pelicula in peliculas:
    if contador == 2:
        print(pelicula['titulo'], pelicula['año'], pelicula['director'])
    contador += 1




