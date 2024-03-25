from turtle import Turtle
t=Turtle()
t.up()
t.backward(220)
t.down()

def star(t,length):
    for i in range(6):
        for i in range(3):
            t.backward(60)
            t.right(36)
            t.forward(60)
            t.right(36)
        t.left(36)
        t.right(180)
        t.up()
        t.forward(160)
        t.down()
    
star(t,20)