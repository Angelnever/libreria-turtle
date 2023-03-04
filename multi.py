import turtle
import random

s = turtle.Screen()
s.title("Carreras")
s.bgcolor("gray")


jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
jugador1.hideturtle()
jugador2.hideturtle()
jugador3 = turtle.Turtle()
jugador3.hideturtle()

jugador1.shape("turtle")
jugador1.color("green","green")

jugador2.shape("turtle")
jugador2.color("blue","blue")

jugador3.shape("turtle")
jugador3.color("red","red")

jugador1.speed(12)
jugador2.speed(12)
jugador3.speed(12)

jugador1.shapesize(2,2,2)
jugador1.pensize(3)
jugador1.penup()
jugador1.goto(200,100)
jugador1.pendown()
jugador1.circle(40)
jugador1.penup()
jugador1.goto(-300,140)

jugador2.shapesize(2,2,2)
jugador2.pensize(3)
jugador2.penup()
jugador2.goto(200,-100)
jugador2.pendown()
jugador2.circle(40)
jugador2.penup()
jugador2.goto(-300,-60)

jugador3.shapesize(2,2,2)
jugador3.pensize(3)
jugador3.penup()
jugador3.goto(200,0)
jugador3.pendown()
jugador3.circle(40)
jugador3.penup()
jugador3.goto(-300,40)

jugador1.showturtle()
jugador2.showturtle()
jugador3.showturtle()

dado = [1,2,3,4,5,6]

for i in range (20):
    if jugador1.pos()>= (180,140):
        print("La tortuga verde a ganado")
        break
    elif jugador2.pos()>= (180,-60):
        print("La tortuga azul a ganado")
        break
    elif jugador3.pos()>= (180,40):
        print("La tortuga roja a ganado")
        break
    else:
        turno1 = input("Turno tortuga verde presiona enter para avanzar: ")
        turno1 = random.choice(dado)
        print(f"Tu numero es: {turno1} \n Avanzas {turno1*20}")
        jugador1.pendown()
        jugador1.fd(20*turno1)
        
        turno2 = input("Turno tortuga azul presiona enter para avanzar: ")
        turno2 = random.choice(dado)
        print(f"Tu numero es: {turno2} \n Avanzas {turno2*20}")
        jugador2.pendown()
        jugador2.fd(turno2*20)
        
        turno3 = input("Turno tortuga roja presiona enter para avanzar: ")
        turno3 = random.choice(dado)
        print(f"Tu numero es: {turno3} \n Avanzas {turno3*20}")
        jugador3.pendown()
        jugador3.fd(turno3*20)

    
turtle.done()