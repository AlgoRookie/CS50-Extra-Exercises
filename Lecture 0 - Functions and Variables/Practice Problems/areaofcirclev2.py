# Write a function area_of_circle(radius) that takes one parameter, radius, and 
# returns the area of a circle (use the formula: area = π * radius²).
# implement improvements from areaofcircle.py

import math

def main():
    # takes the input as a float to allow for arithmetic operation
    rad = float(input("Please enter the radius of the circle in cm: "))
    # passes rad input variable to area of circle function
    area = area_of_circle(rad)
    # print result of arithmetic, formatted to display rounded to 2dp
    print(f"The area is {area:.2f}cm squared")

def area_of_circle(radius):
    # equation of a circle
    # use of math library to avoid manually defining π
    area = math.pi * (radius ** 2)
    # return value stored in area variable
    return area

# calling main function
main()
