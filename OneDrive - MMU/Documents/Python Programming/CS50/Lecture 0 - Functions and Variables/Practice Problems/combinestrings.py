# Write a function combine_strings(s1, s2) that takes two strings s1 and s2 
# and returns a single string that combines them with a space in between.

def main():
    # prompt user to enter two strings
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # combine both inputs
    fullstring = combine_strings(str1, str2)
    print(fullstring)

# function to combine both inputs
def combine_strings(s1, s2):
    return "Full string = " + s1 + " " + s2
     

main()