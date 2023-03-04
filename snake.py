import turtle
import time
import random

retraso = 0.1
cuenta = 0
cuenta_alta = 0

s = turtle.Screen()
s.bgcolor("gray")
s.title("SNAKE")
s.setup(700,500)

serpiente = turtle.Turtle()
serpiente.speed(10)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
serpiente.color("black","green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("red","red")
comida.penup()
comida.goto(100,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,210)
texto.write("Marcador: 0 \t Marcador más alto: 0", align="center", font=("verdana",20,"normal"))

def arriba():
    serpiente.direction = "up"
    
def abajo():
    serpiente.direction = "down"
    
def derecha():
    serpiente.direction = "right"
    
def izquierda():
    serpiente.direction = "left"

def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x-20)
        
s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(izquierda,"Left")
s.onkeypress(derecha,"Right")


while True:
    s.update()
    
    if serpiente.xcor() > 350 or serpiente.xcor() < -350 or serpiente.ycor() > 250 or serpiente.ycor() < -250:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()
        
        cuenta = 0
        texto.clear()
        texto.write("Marcador: {} \t Marcador más alto: {}".format(cuenta,cuenta_alta) ,align="center", font=("verdana",20,"normal"))
        
    if serpiente.distance(comida) < 20:
        x = random.randint(-330,330)
        y = random.randint(-230,230)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green","green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        
        cuenta += 10
        texto.clear()
        texto.write("Marcador: {} \t Marcador más alto: {}".format(cuenta,cuenta_alta) ,align="center", font=("verdana",20,"normal"))
        if cuenta > cuenta_alta:
            cuenta_alta = cuenta
            texto.clear()
            texto.write("Marcador: {} \t Marcador más alto: {}".format(cuenta,cuenta_alta) ,align="center", font=("verdana",20,"normal"))
            
        cuerpo.append(nuevo_cuerpo)
    
    total = len(cuerpo)
    for index in range(total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)
            
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)
        
    movimiento()
    
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"
    time.sleep(retraso)
    
turtle.done()   