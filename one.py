# from turtle import *
# circle(100,steps=6)
# done()

# from turtle import *
# circle(100,120)
# done()

# from turtle import *
# up()
# goto(0,-100)
# down()
# circle(100)
# up()
# done()
# from turtle import *

# speed(0)
# up()
# goto(0,100)
# down()
# circle(-100)
# up()
# goto(50,25)
# down()
# circle(-10)
# up()
# goto(-50,25)
# down()
# circle(-10)
# up()
# goto(40,-30)
# down()
# rt(90)
# circle(-40, 180)

# done()
import turtle

screen = turtle.Screen()
screen.title("Indian National Flag - Tiranga")
screen.bgcolor("white")

flag = turtle.Turtle()
flag.speed(3)

# Constants
FLAG_WIDTH = 600
FLAG_HEIGHT = 400
STRIPE_HEIGHT = FLAG_HEIGHT / 3
ASHOKA_RADIUS = 40

def draw_rectangle(color, x, y, width, height):
    flag.penup()
    flag.goto(x, y)
    flag.color(color)
    flag.begin_fill()
    flag.pendown()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

def draw_chakra(radius):
    flag.penup()
    flag.goto(0, STRIPE_HEIGHT/2 - radius)
    flag.setheading(0)
    flag.pendown()
    flag.color("navy")
    flag.width(2)
    flag.circle(radius)

    # Draw 24 spokes
    flag.penup()
    flag.goto(0, STRIPE_HEIGHT/2)
    for i in range(24):
        flag.setheading(i * 15)
        flag.pendown()
        flag.forward(radius)
        flag.penup()
        flag.goto(0, STRIPE_HEIGHT/2)

# Draw the three stripes of the flag
start_x = -FLAG_WIDTH / 2
start_y = FLAG_HEIGHT / 2

# Top stripe - Saffron
draw_rectangle("orange", start_x, start_y, FLAG_WIDTH, STRIPE_HEIGHT)

# Middle stripe - White
draw_rectangle("white", start_x, start_y - STRIPE_HEIGHT, FLAG_WIDTH, STRIPE_HEIGHT)

# Bottom stripe - Green
draw_rectangle("green", start_x, start_y - 2 * STRIPE_HEIGHT, FLAG_WIDTH, STRIPE_HEIGHT)

# Draw Ashoka Chakra
draw_chakra(ASHOKA_RADIUS)

# Optional flagpole
flag.penup()
flag.goto(start_x, start_y)
flag.setheading(-90)
flag.pensize(10)
flag.color("gray")
flag.pendown()
flag.forward(FLAG_HEIGHT + 100)

flag.hideturtle()
turtle.done()
