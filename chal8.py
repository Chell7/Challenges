#CHALLENGES 60-68
#60
import turtle 
for i in range (4) :
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()

#61
import turtle 
for i in range(3) :
    turtle.left(120)
    turtle.forward(100)

turtle.exitonclick()

#62
import turtle 
for i in range(360) :
        turtle.forward(1)
        turtle.right(1)

turtle.exitonclick()

#63
import turtle 
turtle.color('green')
turtle.begin_fill()
for i in range (4) :
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
    
turtle.pendown
turtle.color('yellow')
turtle.begin_fill()
for i in range (4) :
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown
turtle.color('black')
turtle.begin_fill()
for i in range (4) :
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.exitonclick()

#64
import turtle 
for i in range (5) :
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()

#65
import turtle

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.hideturtle()

turtle.exitonclick()

#66
import turtle
import random

turtle.pensize(4)

for i in range (0,8) :
    turtle.color(random.choice(['red','orange','green', 'blue', 'black', 'pink']))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()

#67
import random
import turtle

for x in range (0,10) :
    for i in range (0, 8) :
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()

turtle.exitonclick()

#68
import turtle
import random

lines= random.randint(5,20)

for y in range (0,lines) :
    length = random.randint(25, 100)
    rotate= random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick
