# Section 13
# CSE 231, project 01

# Get a number from the user and set it to a variable, gallons.  Convert the
# string to a float number.
gallons = float(raw_input("How many gallons of gasoline? "))

# Prints calculations in several lines
print "Original number of gallons: ", gallons
print "Liters:", 3.7854 * gallons
print "Barrels of oil required: ", gallons / 19.5
print "Pounds of CO2 produced: ", gallons * 20
print "Gallons of ethanol: ", gallons * 115000 / 75700
print "It costs $", gallons * 4, "!!!  Yowch."
print "Thank you!"
