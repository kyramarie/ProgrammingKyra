import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Make multiple squares")

jan = turtle.Turtle()
jan.color("blue")
jan.pensize(3)

def draw_square (animal, size):
    for _ in range(4):
        animal.forward(200)
        animal.left(90)

for _ in range(17):
    draw_square(jan, 200)
    jan.left(22.5)

window.mainloop()
