from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    name = input("Enter your name: ")
    number = int(input("Enter a number: "))
    parity = "even" if is_even(number) else "odd"

    print(greet(name))
    print(f"Square: {square(number)}")
    print(f"The number is {parity}.")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")


if __name__ == "__main__":
    main()