#EXERCICE 11


import turtle

def draw_spiral(turns):
    """"""
    epaisseur = 2
    turtle.width(epaisseur)
    for i in range(turns * 2):  # chaque tour a 2 demi-cercles
        turtle.circle(20 * (i + 1) // 2, 90)  # demi-circle
        epaisseur += 1
        turtle.width(epaisseur)

# Test spiral
turtle.speed(0)
draw_spiral(10)
turtle.done()
