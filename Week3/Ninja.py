import turtle

#create paper to draw on
paper = turtle.Screen()

#create the ninja
leonardo = turtle.Turtle()
leonardo.color("red")

#Ask it to move forward 50 steps
leonardo.forward(50)

#let it do other stuff
leonardo.stamp()
leonardo.penup()
leonardo.forward(50)
leonardo.pendown()
leonardo.stamp()

leonardo.forward(50)

leonardo.left(60)
leonardo.forward(50)

#so that the drawing sticks around and does not immediately disappear
paper.exitonclick()


