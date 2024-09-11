import math

print("Find the area and perimeter of your circle")
radius = float(input("What is your circle's radius"))

area1 = (math.pi*(radius**2))
area = round(area1, 2)

circ1 = (math.pi *2 * radius)
circ = round(circ1, 2)

print(f"For a circle with a radius of {radius} the area is {area} and perimeter is {circ}")
