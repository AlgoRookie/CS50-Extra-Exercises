# Write a function category(age) that takes an integer age.
# Print "Child" if age is less than 13.
# Print "Teenager" if age is between 13 and 19 (inclusive).
# Print "Adult" if age is 20 or above.

def main():
    usrage = int(input("How old are you? "))
    category(usrage)

def category(age):
    if age < 13:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    else:
        print("Adult")

if __name__ == "__main__":
    main()