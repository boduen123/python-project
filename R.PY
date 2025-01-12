import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # Set speed to maximum
bgcolor("black")
color("#f73487")  # Set color for drawing
penup()  # Lift the pen to move to the starting position
goto(0, 0)  # Move to the center
pendown()  # Start drawing

for i in range(0, 6000):
    k = i / 100  # Scale down the loop variable
    goto(hearta(k) * 20, heartb(k) * 20)

done()  # Finish drawing
