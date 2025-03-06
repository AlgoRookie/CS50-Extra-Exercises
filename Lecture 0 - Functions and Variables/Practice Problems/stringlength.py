# Write a function string_length(s) that takes a string s 
# and returns the length of the string.

def main():
    # use of .strip() ensures whitespace doesn't count as a character
    string = input("Enter a word/phrase here: ")
    print(string_length(string))


def string_length(s):
    # use built-in len() function to determine string length
    return len(s.replace(" ", ""))

main()