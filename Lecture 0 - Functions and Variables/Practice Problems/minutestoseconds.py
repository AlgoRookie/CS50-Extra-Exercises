# Write a function minutes_to_seconds(minutes) that takes one 
# parameter minutes and converts it into seconds (multiply by 60).
def main():
    # prompt user to enter a minutes value
    mins = int(input("Enter minutes: "))
    # pass mins value as an argument into function
    # store result in secs variable
    secs = minutes_to_seconds(mins)
    # print result
    print(secs, "seconds")

# function to convert from mins to secs
def minutes_to_seconds(minutes):
    # multiply seconds by 60
    seconds = minutes * 60
    return seconds

# call main function
main()