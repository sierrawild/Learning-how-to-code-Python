from turtle import *
import random

hideturtle()
speed(0)

for i in range(10):
    forward(random.randint(2,100))
    right(90)
    
    x,y = pos()
    
print(f"{x=} {y=}")

    

exitonclick()