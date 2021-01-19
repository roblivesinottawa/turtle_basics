import turtle

item = turtle.Turtle()
# item.forward(100)
# item.left(45)
# item.forward(100)
# item.right(45)
# item.forward(100)

# can use hex values 
item.color("#3c9118", "red")

# fills the inside with a color
item.begin_fill()
# this creates a square
item.forward(100)
item.left(90)
item.forward(100)
item.left(90)
item.forward(100)
item.left(90)
item.forward(100)


# this moves the pen down and creates another square
item.penup()
item.forward(150)
item.pendown()

item.forward(100)
item.left(90)
item.forward(100)
item.left(90)
item.forward(100)
item.left(90)
item.forward(100)

item.end_fill()




turtle.done()