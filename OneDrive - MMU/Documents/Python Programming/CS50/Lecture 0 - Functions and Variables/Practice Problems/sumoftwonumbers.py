# Write a function sum_of_two_numbers(a, b) that takes two parameters, 
# a and b, and returns their sum.

def main():
    # prompt the user to enter 2 numbers
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter your second number: "))
    # call function to sum numbers together and print result
    print(sum_of_two_numbers(n1, n2))
    
# function responsible for summing numbers together
def sum_of_two_numbers(a, b):
    sum = a + b
    return sum

# call main function to run
main()
