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

    count = 0
    while( count < 3 ):
        start.backward(100)
        start.left(120)
        count = count + 1
    


def main_program():
    window = turtle.Screen()
    window.bgcolor("grey")
    
    # draw a square
    draw_square()
    draw_circle()
    draw_triangle()
    draw_square_fractal()
    window.exitonclick()
    
main_program()
