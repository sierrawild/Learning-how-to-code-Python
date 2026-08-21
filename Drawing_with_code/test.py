import turtle

t = turtle.Turtle()
t.speed(0)

this_thing = 0

while this_thing < 400:
    
    t.fd(100 + this_thing)
    t.right(89)
    this_thing = this_thing + 1
    print(this_thing)
    
    


turtle.done()