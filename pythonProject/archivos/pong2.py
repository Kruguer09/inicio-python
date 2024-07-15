#juego del pong
# Importar librerias
import turtle
import os

# puntuaión
puntosJugador1 = 0
puntosJugador2 = 0
# funciones
def raqueta1_up():
    y = raqueta1.ycor()
    y += 20
    raqueta1.sety(y)
def raqueta1_down():
    y = raqueta1.ycor()
    y -= 20
    raqueta1.sety(y)
def raqueta2_up():
    y = raqueta2.ycor()
    y += 20
    raqueta2.sety(y)
def raqueta2_down():
    y = raqueta2.ycor()
    y -= 20
    raqueta2.sety(y)

# Configurar la ventana
ventana = turtle.Screen()
ventana.title("PONG - Josele")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0) # Desactiva las actualizaciones de la pantalla, lo hace más visual

# Raqueta A
raqueta1 = turtle.Turtle()
raqueta1.speed(0)
raqueta1.shape("square")
raqueta1.color("white")
raqueta1.shapesize(stretch_wid=8, stretch_len=1) #8*20 , 1*20 pixeles
raqueta1.penup()
raqueta1.goto(350,200)
# Raqueta B
raqueta2 = turtle.Turtle()
raqueta2.speed(0)
raqueta2.shape("square")
raqueta2.color("white")
raqueta2.shapesize(stretch_wid=8, stretch_len=1) #8*20 , 1*20 pixeles
raqueta2.penup()
raqueta2.goto(-350,-200)
# marcador
marcador = turtle.Turtle()
marcador.color("white")
marcador.speed(0)
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("Jugador A: {}  Jugador B: {}".format(puntosJugador1,puntosJugador2), align="center", font=("Courier", 18, "normal"))

# Pelota
pelota = turtle.Turtle()
pelota.speed(1)
pelota.shape("circle")
pelota.color("yellow")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.3
pelota.dy = 0.3




# Teclado
ventana.listen()
ventana.onkeypress(raqueta2_up, "w")
ventana.onkeypress(raqueta2_down, "s")
ventana.onkeypress(raqueta1_up, "Up")
ventana.onkeypress(raqueta1_down, "Down")

# Bucle principal
while True:
    ventana.update() # Actualiza la pantalla
    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    # Colisiones con el borde superior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    # Colisiones con el borde inferior
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
    # Accion en el borde derecho
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntosJugador1 += 1
        marcador.clear()
        marcador.write("Jugador A: {}  Jugador B: {}".format(puntosJugador1, puntosJugador2), align="center", font=("Courier", 18, "normal"))

    # Accion en el borde izquierdo
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntosJugador2 += 1
        marcador.clear()
        marcador.write("Jugador A: {}  Jugador B: {}".format(puntosJugador1, puntosJugador2), align="center", font=("Courier", 18, "normal"))
    # Colisiones con la raqueta derecha
    if (pelota.xcor()>335) and (pelota.ycor()<raqueta1.ycor()+80 and pelota.ycor()>raqueta1.ycor()-80):
        pelota.setx(330)
        pelota.dx *= -1
        # sonido de colisión

    # Colisiones con la raqueta izquierda
    if (pelota.xcor()<-335) and (pelota.ycor()<raqueta2.ycor()+80 and pelota.ycor()>raqueta2.ycor()-80):
        pelota.setx(-330)
        pelota.dx *= -1
        # sonido de colisión






