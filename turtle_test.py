
#setup
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")
t.speed(9)

#set up screen
#turtle.bgcolor("blue")
turtle.title("Hunter's Game")
#
#u = input("Would you like me to draw a shape? Type yes or no: ")
#if u == "yes":
#    t.penup()
#    t.goto(200,200)
#    t.pendown()
#    n=10
#    while n <= 100:
#        t.circle(n)
#        n = n+10
#     t.circle(50)
# elif u == "no":
#     print("Okay")
# else:
#     print("Invalid Reply")
#first circles


# circles 1
t.penup()
t.goto(-200,-200)
t.pendown()
n=10
while n <= 100:
    t.circle(n)
    n = n+10

# circles 1
t.penup()
t.goto(-200,200)
t.pendown()
n=10
while n <= 100:
    t.circle(n)
    n = n+10

# circles 1
t.penup()
t.goto(200,200)
t.pendown()
n=10
while n <= 100:
    t.circle(n)
    n = n+10


# circles 1
t.penup()
t.goto(200,-200)
t.pendown()
n=10
while n <= 100:
    t.circle(n)
    n = n+10
#done()

#other commands
# t.forward(100)
# t.right(90)
# t.left(100)
# t.backward(100)

# turtle.bgcolor(hexcode)
# t.home()
# t.circle(100)
# t.dot(30)
# t.shapesize(1,5,10) : stretch lengths, stretch width, outline width
# t.pensize(5)
# t.fillcolor(hex code)
# t.pencolor(hex code)
# changes both fill and pen color t.color("green", "red")
#t.penup()
# t.pendown()
# t.undo()
# t.clear()
# t.reset()

#fill an image
#t.begin_fill()
# t.fd(100)
#t.lt(120)
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.end_fill()

# turtle shapes

# t.shape("turtle")
# t.shape("arrow")
# t.shape("circle")
# Square, Triangle, Classic

#clone Turtle
# c = t.clone()

#for loop Square
#for i in range(4):
#     t.fd(100)
#     t.rt(90)

# u = input("Would you like me to draw a shape? Type yes or no: ")
# if u == "yes":
#     t.circle(50)


# u = input("Would you like me to draw a shape? Type yes or no: ")
# if u == "yes":
#     t.circle(50)
# elif u == "no":
#     print("Okay")
# else:
#     print("Invalid Reply")
