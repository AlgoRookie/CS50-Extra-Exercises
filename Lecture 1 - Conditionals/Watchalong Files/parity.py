def main():
    x = int(input("What is x?: "))
    print(odd_or_even(x))


def odd_or_even(int):
    return("X is even") if int % 2 == 0 else ("X is odd")

main()