# Lab 4 - File 2 - Sep 18
# Group Members – Mairi Weber-Hess, Aliza Litvak

import turtle

ted = turtle.Turtle()
ted.color("yellow")

for side in range(4):
    if side == 1:
        ted.color("forest green")
    if side == 3:
        ted.color("royal blue")
    ted.forward(150)
    ted.right(90)