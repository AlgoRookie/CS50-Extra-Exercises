# Write a function day_of_week(day_number) that takes an integer day_number from 1 to 7.
# Print the corresponding day of the week (e.g., 1 = "Monday", 2 = "Tuesday", etc.).
# Print "Invalid Input" if the number is outside the range.

def main():
    day = int(input("Enter a number from 1-7: "))
    day_of_week(day)


def day_of_week(int):
    match int:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid Input")

if __name__ == "__main__":
    main()