# Write a function swap_variables(a, b) that takes two variables a and b 
# and swaps their values. The function should return the swapped values.
# implement improvements from swapvariables.py

def main():
    # take inputs from user
    var1 = input("A = ")
    var2 = input("B = ")

    # prints before to notice changes
    print(f"Before: A = {var1}, B = {var2}")

    # unpack variables from function
    var1, var2 = swap_variables(var1, var2)

    # prints after to verify changes
    print(f"After: A = {var1}, B = {var2}")

# function to swap the variables
def swap_variables(a, b):
    return b, a

main()