import turtle
t = turtle.Turtle()

#function
def square( x , y):
    
    t.forward(x)
    t.right(y)
    t.color("red")
    t.forward(x)
    t.right(y)
    t.color("blue")
    t.forward(x)
    t.right(y)
    t.color("green")
    t.forward(x)



square(50, -90)
square(70, 60)
square(90, 20)
square(110,70)
t.circle(50)
while(True):
    print(".")


