#EXERCICE 10

import turtle

def rect(width, height, color):
    """Dessine un rectangle avec la largeur, la hauteur et la couleur données."""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_flag_guinea():
    """Dessine le drapeau de la Guinée."""
    turtle.penup()
    colors = ["red", "yellow", "green"]
    for i, color in enumerate(colors):
        turtle.goto(i * 50, 0)
        turtle.pendown()
        rect(50, 100, color)
        turtle.penup()

def draw_flag_germany():
    """Dessine le drapeau de l'allemagne"""
    turtle.penup()
    colors = ["black", "red", "yellow"]
    for i, color in enumerate(colors):
        turtle.goto(0, -i * 30)
        turtle.pendown()
        rect(100, 30, color)
        turtle.penup()

def draw_flag_sweden():
    """dessine le drapeau de la Suède"""
    turtle.penup()
    turtle.goto(-50, -50)
    rect(100, 60, "blue")
    turtle.goto(-30, -50)
    rect(20, 60, "yellow")
    turtle.goto(-50, -30)
    rect(100, 20, "yellow")
    turtle.penup()

# Test flags
turtle.speed(3)
draw_flag_guinea()
turtle.clear()
draw_flag_germany()
turtle.clear()
draw_flag_sweden()
turtle.done()
