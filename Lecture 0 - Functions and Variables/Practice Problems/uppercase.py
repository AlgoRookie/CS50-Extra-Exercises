# Write a function uppercase_string(s) that takes a string s and 
# returns the string with all characters in uppercase.

def main():
    string = input("Please enter a word/phrase: ")
    print(uppercase(string))

def uppercase(s):
    return s.upper()

main()