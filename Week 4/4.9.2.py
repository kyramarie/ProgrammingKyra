import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Make multiple squares")

jan = turtle.Turtle()
jan.color("hotpink")
jan.pensize(5)

def draw_square (animal, size):
    """
    make Jan draw a square
    """
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

size = 50
for _ in range(5):
    draw_square(jan, size)
    jan.penup()
    jan.right(135)
    jan.forward(20)
    jan.left(135)
    size += 30
    jan.pendown()


window.mainloop()