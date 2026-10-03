from utils import celsius_to_fahrenheit, is_even, square


def main():
    number = int(input("Enter a number: "))
    parity = "even" if is_even(number) else "odd"

    print(f"Square: {square(number)}")
    print(f"The number is {parity}.")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")


if __name__ == "__main__":
    main()