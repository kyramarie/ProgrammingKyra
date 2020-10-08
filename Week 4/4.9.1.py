import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Make multiple squares")

jan = turtle.Turtle()
jan.color("hotpink")
jan.pensize(5)

def draw_square (animal, size):
    """
    make animal draw a square with sides of length size. 
    """
    for _ in range (4):
        animal.forward(size)
        animal.left(90)

for _ in range(5):
    draw_square(jan, 50)
    jan.penup()
    jan.forward(100)
    jan.pendown()


window.mainloop()
