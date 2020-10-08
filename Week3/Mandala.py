import turtle

paper = turtle.Screen()
carl = turtle.Turtle()
carl.shape("turtle")

colors = ['red','orange','yellow','green','blue']

for element in range(12):
    carl.color(colors[element % len(colors)])
    if element % 2 == 0:
        leonardo.forward(100)
    else:
        leonardo.forward(50)
    leonardo.left(30)
    print(element)