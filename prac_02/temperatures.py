# temperatures.py
# Program to convert between Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}C = {celsius_to_fahrenheit(celsius):.2f}F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}F = {fahrenheit_to_celsius(fahrenheit):.2f}C")


main()