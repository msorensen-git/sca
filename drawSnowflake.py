import turtle
import random
colors = ["blue", "cyan", "yellow", "purple","orange", "red"]

pat = turtle.Turtle()

#for i in range(10):
#    for j in range(2):
#        pat.color(random.choice(colors))
#        pat.forward(100)
#        pat.right(60)
#        pat.forward(100)
#        pat.right(120)
#    pat.right(36)
turtle.Screen().bgcolor("grey")

pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()
    
def branch():
    for i in range(3):
        for i in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)

for i in range(8):
    branch()
    pat.left(45)
    