import turtle

item = turtle.Turtle()

item.color("red", "yellow")
item.speed(10)

item.begin_fill()
for i in range(50):
    item.forward(300)
    item.left(170)

item.end_fill()






turtle.done()