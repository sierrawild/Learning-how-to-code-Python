from turtle import *
import random

hideturtle()
speed(0)
random.seed(1)

xx, yy = 150, 250

for i in range(1000):
    forward(random.randint(2,100))
    right(90)
    
    x,y = pos()
    
    if x > xx:
        setheading(180)
        forward(random.randint(50,100))
    elif x < -xx:
        setheading(0)
        forward(random.randint(50,100))
    elif y > yy:
        setheading(270)
        forward(random.randint(50,100))
    elif y < -yy:
        setheading(90)
        forward(random.randint(50,100))
        
    
    
print(f"{x=} {y=}")

    

exitonclick()