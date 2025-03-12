# Write a function reverse_string(s) that takes a string s 
# and returns the string reversed.

def main():
    # prompt user to input
    string = input("Enter a word: ")
    print (reverse_string(string).capitalize())

def reverse_string(s):
    # using slice to start at end of string and move to position 0 with step -1
    return s [::-1]

main()