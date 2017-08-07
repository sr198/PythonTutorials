import turtle

def draw_square_fractal():
    window = turtle.Screen()
    window.bgcolor("red")
    
    start = turtle.Turtle()
    start.shape("turtle")
    start.speed(50)
    start.color("white")

    count = 0
    while( count < 180 ):        
        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.right(2)
        count = count + 1

    window.exitonclick()

def draw_square():    
    start = turtle.Turtle()
    start.shape("turtle")
    start.speed(5)
    start.color("white")

    count = 0
    while( count < 4 ):
        start.forward(100)
        start.right(90)
        count = count + 1

def draw_circle():
    start = turtle.Turtle()
    start.shape("arrow")
    start.speed(2)
    start.color("red")

    start.circle(100)

def draw_triangle():
    start = turtle.Turtle()
    start.shape("arrow")
    start.speed(2)
    start.color("blue")
    window = turtle.Screen()
    window.bgcolor("red")
    
    start = turtle.Turtle()
    start.shape("turtle")
    start.speed(50)
    start.color("white")

    count = 0
    while( count < 180 ):        
        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.forward(100)
        start.right(90)

        start.right(2)
        count = count + 1

    window.exitonclick()


def draw_triangle_fractal(startX, startY, edgeSize):
    window = turtle.Screen()
    window.bgcolor("white")
    
    start = turtle.Turtle()
    start.shape("turtle")
    start.speed(1)
    start.color("red")

    #draw base triangle first
    start.penup()
    start.setpos(startX, startY)
    
    start.pendown()
    start.forward(edgeSize)
    start.left(120)
    start.forward(edgeSize)
    start.left(120)
    start.forward(edgeSize)
    
    start.left(180)
    start.forward(edgeSize/2)
    start.right(60)

    start.forward(edgeSize/2)
    start.right(120)
    start.forward(edgeSize/2)
    start.right(120)
    start.forward(edgeSize/2)

    start.penup()
    start.backward(edgeSize/4)
    start.pendown()
    draw_triangle(start, edgeSize/4, 1)
##
##    start.penup()
##    start.setx(start.xcor()+(edgeSize/4))
##    start.pendown()
##    draw_triangle(start, edgeSize/4, "right",1)
##
##    start.penup()
##    start.forward(edgeSize/4)    
##    start.pendown()
##    draw_triangle(start, edgeSize/4, "top",1)
##
##    start.penup()
##    start.
##    start.pendown()
    window.exitonclick()

def draw_triangle(start, edge, level):
    start.setheading(0)
    level = level + 1

    if( level == 3 ):
        return
    
    #draw triangle on the left
    start.left(180)
    start.forward(edge)
    start.left(120)
    start.forward(edge)
    start.left(120)
    start.forward(edge)
    draw_triangle( start, edge/2, level)

    #triangle on the right
    start.forward(edge)
    start.right(120)
    start.forward(edge)
    start.right(120)
    start.forward(edge)
    draw_triangle( start, edge/2, level)
    
    #triangle on the top
    start.left(60)
    start.forward(edge)
    start.left(120)
    start.forward(edge)
    start.left(120)
    start.forward(edge)
    draw_triangle( start, edge/2, level)
    
def main_program():
   draw_triangle_fractal(0.0,0.0,400)
    
main_program()
