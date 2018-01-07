# simple turtle graphics
# draw a square, draw a circle
# wfp, 9/2/08

import turtle

# title for the display window
turtle.title("Fun with Turtle Graphics and Python")

turtle.up()        # lift the pen up, no drawing
turtle.goto(50,50)
turtle.down()      # pen is down, drawing now

# draw the square
turtle.goto(50,250)
turtle.goto(250,250)
turtle.goto(250,50)
turtle.goto(50,50)

# draw the circle
turtle.up()
turtle.goto(150,50)
turtle.down()
turtle.circle(100)

# go to the center, leave a message
turtle.up()
turtle.goto(150,150)
turtle.write('Hi')

# IMPORTANT, must do this to finish the drawing
turtle.done()
