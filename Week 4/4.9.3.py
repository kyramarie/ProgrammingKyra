import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Make multiple squares")

jan = turtle.Turtle()
jan.color("hotpink")
jan.pensize(5)

def draw_poly (animal, n, sz):
    for _ in range(8):
        animal.forward(80)
        animal.left(45)

draw_poly(jan, 8, 50)

window.mainloop()