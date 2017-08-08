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
    start.speed(5)
    start.color("red")

    #draw base triangle first
    start.penup()
    start.setpos(startX, startY)
    
    start.pendown()
    start.color("red","yellow")
    start.begin_fill()
    start.forward(edgeSize)
    start.left(120)
    start.forward(edgeSize)
    start.left(120)
    start.forward(edgeSize)
    start.end_fill()
    start.backward(edgeSize/2)
    draw_triangle(start, edgeSize/2, 0)

    start.penup()
    start.setpos(startX,startY)
    
    window.exitonclick()


def draw_triangle(start, edge, level):
    parent_x=start.xcor()
    parent_y=start.ycor()
    
    #draw the triangle
    start.color("red","green")
    start.setheading(0)
    start.begin_fill()
    start.forward(edge)
    start.right(120)
    start.forward(edge)
    start.right(120)
    start.forward(edge)
    start.end_fill()
    #terminating condition
    level = level + 1
    if( level == 4):
        return

    #draw triangle on the left with edge/2 sides
    #locate the left starting point
    start.setheading(0)
    start.penup()
    start.right(120)
    start.forward(edge/2)
    start.pendown()
    draw_triangle( start, edge/2, level )
    #reset start to parent
    start.penup()
    start.setx(parent_x)
    start.sety(parent_y)
    start.pendown()
    
    #triangle to the right
    start.setheading(0)
    start.penup()
    start.forward(edge)
    start.right(120)
    start.forward(edge/2)
    start.pendown()
    draw_triangle( start, edge/2, level)
    #reset start to parent
    start.penup()
    start.setx(parent_x)
    start.sety(parent_y)
    start.pendown()
    
    #triangle on the top
    start.setheading(0)
    start.penup()
    start.left(60)
    start.forward(edge/2)
    start.pendown()
    draw_triangle( start, edge/2, level)    

def main_program():
   draw_triangle_fractal(-200.0,-200.0,800)
    
main_program()
