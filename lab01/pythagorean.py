import math
print("Calculate the hypotenuse of your right triangle.")
side_one = float(input("Please enter a number for the first triangle side. "))
side_two = float(input("Please enter a number for the second triangle side. "))

cpower = ((side_one**2)+(side_two**2))
hypo = math.sqrt(cpower)

limited_float = round(hypo, 2)
print("Your hypotenuse is " , limited_float)
