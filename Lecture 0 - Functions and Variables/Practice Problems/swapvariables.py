# Write a function swap_variables(a, b) that takes two variables a and b 
# and swaps their values. The function should return the swapped values.
def main():
    var1 = input("A = ")
    var2 = input("B = ")
    print("Before A =", var1, "Before B =", var2)
    print(swap_variables(var1, var2))

# function to swap the variables
def swap_variables(a, b):
    # hold the variables in temporary swaps
    swap1 = a
    swap2 = b
    # assign the swaps to the opposite variables
    a = swap2
    b = swap1
    return a, b

main()

## improvements
## unpack variables from function called in main so they don't print as tuple
## don't use swap variables initate swap through return