# Write a function check(temp) that takes an integer temp representing the temperature in degrees Celsius.
# If the temperature is above 30, print "It's hot!".
# If it's between 15 and 30 (inclusive), print "It's warm.".
# If it's below 15, print "It's cold!".

def main():
    # prompt user input
    temp = int(input("What is the temperature? (C) "))
    # pass input through function
    print(check(temp))

def check(degrees):
    if degrees > 30:
        return("It's hot!")
    elif 15 <= degrees <= 30:
        return("It's warm.")
    else:
        return("It's cold!")

if __name__ == "__main__":
    main()