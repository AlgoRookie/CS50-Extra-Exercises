# Write a function area_of_circle(radius) that takes one parameter, radius, and 
# returns the area of a circle (use the formula: area = π * radius²).

def main():
    # takes the input as a float to allow for arithmetic operation
    rad = float(input("Please enter the radius of the circle in cm: "))
    # passes rad input variable to area of circle function
    area = area_of_circle(rad)
    # print result of arithmetic, formatted to display rounded to 2dp
    print(f"The area is {area:.2f}cm squared")

def area_of_circle(radius):
    # defined constant for pi
    π = 3.141592653589793238462643383279502884197169399375105820974944592
    # equation of a circle
    area = π * (radius ** 2)
    # return value stored in area variable
    return area

# calling main function
main()


## improvements 
## use math.pi instead of defining value for π manually