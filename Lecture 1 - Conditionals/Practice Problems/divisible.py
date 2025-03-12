# Write a function divisibility(number) that takes an integer number.
# Print "Divisible by 3" if the number is divisible by 3.
# Print "Divisible by 5" if the number is divisible by 5.
# Print "Divisible by 3 and 5" if the number is divisible by both.
# Print "Not Divisible" if none of the above conditions are met.

def main():
    x = int(input("Enter a number: "))
    divisibility(x)

def divisibility(number):
    if number % 3 == 0 and number % 5 != 0:
        print("Divisible by 3")
    elif number % 3 != 0 and number % 5 == 0:
        print("Divisible by 5")
    elif number % 3 == 0 and number % 5 == 0:
        print("Divisble by 3 and 5")
    else:
        print("Not Divisible")

if __name__ == "__main__":
    main()