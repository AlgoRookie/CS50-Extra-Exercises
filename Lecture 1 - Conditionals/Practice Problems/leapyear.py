# Write a function leap_year(year) that takes an integer year.
# Print "Leap Year" if the year is divisible by 4 but not by 100, or if it's divisible by 400.
# Otherwise, print "Not a Leap Year".

def main():
    usryear = int(input("Enter a year: "))
    leap_year(usryear)

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("It's a leap year.")
    else:
        print("It's not a leap year.")
        
        
if __name__ == "__main__":
    main()