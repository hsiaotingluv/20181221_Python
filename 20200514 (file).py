#Chapter 7 turtle
'''
import turtle
t = turtle.Turtle()
'''

#line
'''
t.forward(100) #100 pixels
t.left(45) #45 degree anticlockwise
t.forward(100)
t.right(90)
t.forward(100)
'''

#double squares
'''
t.color("#F76EFF", "#FFEBFF") #hex value

t.begin_fill()

for i in range(4):
    t.forward(100)
    t.left(90)

t.setheading(270)
t.penup()
t.forward(100)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)
    
t.end_fill()
'''

#flower
'''
t.speed(10)

t.color("red", "yellow")

t.begin_fill()

for i in range(100):
    t.forward(300)
    t.left(170)

t.end_fill()
'''   

#random math
'''
import math

t.speed(10)

for i in range(2000):
    t.forward(math.sqrt(i))
    t.left(i % 180)
'''

#stars
'''
t.getscreen().bgcolor("#744747")
t.color("white")
t.speed(10)

t.penup()
t.goto((-200, 100))
t.pendown()

def star(t, size):
    if size < 10:
        return
    else:
        for i in range(5):
            t.forward(size)
            star(t, size / 3)
            t.left(216)
       
star(t, size = 360)
'''
'''
turtle.done()
'''

#radialHexagons
'''
def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

def radialPattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)
'''

#random turtle walk
'''
from turtle import Turtle
import random

def randomWalk(t, turns, distance = 20):
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
        t.forward(distance)
        
def main():
    t = Turtle()
    t.shape("turtle") #shape of cursel
    randomWalk(t, 40, 30)

main()
'''

#randompatterns.py
'''
from turtle import Turtle
import random

def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

def radialPattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

def drawPattern(t, x, y, n, length, shape):
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    fillcolor = colors[random.randint(0, len(colors) -1)]
    t.fillcolor(fillcolor)
    radialPattern(t, n, length, shape)
    t.end_fill()

def main():
    t = Turtle()
    t.speed(10)
    n = 10
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    length = 30
    inset = length * 2
    #upper-left corner
    drawPattern(t, -width + inset, height - inset, n, length, square)
    #lower-left corner
    drawPattern(t, -width + inset, inset - height, n, length, square)

    length = 20
    inset = length * 3
    #upper-right corner
    drawPattern(t, width - inset, height - inset, n, length, hexagon)
    #lower-right corner
    drawPattern(t, width - inset, inset - height, n, length, hexagon)
    
main()
'''

#Chapter 7 exercises
#3 circle
'''
def circle(t, length):
    for i in range(360):
        t.forward(length)
        t.left(1)
'''

#4 n-polygon
'''
def polygon(t, sides, length):
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
'''

#circle
'''
from turtle import Turtle
t = Turtle()

def filledCircle(radius, extent = None, steps = None):
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(radius, extent, steps)
    t.end_fill()
'''
