# proj 02
# CSE 231, section 13

import turtle
import math

print "This program will draw two lines using the origin (0,0)\
and coordinates provided by the user.\
It will then measure the acute angle between the two lines.\
"

# Gets the (x,y) coordinates from the user for each of the two points
print "Can I have coordinates for point 1?"
x1 = float(raw_input("x: "))
y1 = float(raw_input("y: "))
print ""
print x1, ",", y1, "? Thanks!  Now how about the coordinates of point 2?"
x2 = float(raw_input("x: "))
y2 = float(raw_input("y: "))
print ""
print x2, ",", y2, ". Okay then, let's go!!!"

# Calculate the slopes
slope1 = (y2 - y1) / (x2 - x1)
slope2 = (y1 - 0) / (x1 - 0)

# Use the slope values to calculate the tangent
tangent = (abs(slope1 - slope2)) / (1 + slope1 * slope2)

# Take the inverse of the tangent to calculate the angle in radians, then convert to degrees
angle_in_radians = math.atan(tangent)
angle_in_degrees = (angle_in_radians) * 180 / math.pi

strAngle = str(angle_in_degrees) + " degrees"

# title for the display window
turtle.title("Lines and Angles and all that Cool Stuff")

turtle.up()       # lift the pen up, no drawing
turtle.goto(0,0)
turtle.down()     # pen is down, drawing now

# Draw the first line
turtle.goto(0,0)
turtle.goto(x1,y1)

# Draw the second line
turtle.goto(x2,y2)

# Write the angle measurement
turtle.write(strAngle)

# IMPORTANT, must do this to finish the drawing or you'll get an infinite loop
# and you'll have to CTRL-ALT-DEL to close it!  Blech!
turtle.done()

# note: check (30, 100) for the first point and (10, 150) for the second point
