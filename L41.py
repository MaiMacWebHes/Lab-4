# Lab 4 - File 1 - Sep 18
# Group Members – Mairi Weber-Hess, Aliza Litvak

import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)