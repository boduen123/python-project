import turtle
import colorsys

# Initialize the turtle and screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')  # Set background color
t.speed(0)  # Set the fastest drawing speed

n = 70  # Number of color changes
h = 0  # Initial hue

# Draw the pattern
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)  # Convert HSV to RGB
    h += 1/n  # Increment hue
    t.color(c)  # Set the turtle color
    t.left(1)  # Turn left
    t.fd(1)  # Move forward

    for j in range(2):     
        t.left(2)  # Slightly turn left
        t.circle(10)  # Draw a circle

# Finish the drawing
turtle.done()  # Keep the window open
