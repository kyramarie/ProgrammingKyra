import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red','orange','yellow','green','blue']

#can also use:
#use % for color as there is 5 elements in the list
#len stands for lenght of the list
for element in range(12):
    leonardo.color(colors[element % len(colors)])
    if element % 2 == 0:
        leonardo.forward(100)
    else:
        leonardo.forward(50)
    leonardo.left(30)
    print(element)

#double equal sign is a comparison of left to right


paper.exitonclick()