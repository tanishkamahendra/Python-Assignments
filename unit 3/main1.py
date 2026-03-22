from celsius_to_fahrenheit import celsius_to_fahrenheit
from fahrenheit_to_celsius import fahrenheit_to_celsius
from celsius_to_kelvin import celsius_to_kelvin

def main():
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter your choice: ")

    if choice == "1":
        celsius = float(input("Enter Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print("Result:", round(result, 2), "F")

    elif choice == "2":
        fahrenheit = float(input("Enter Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print("Result:", round(result, 2), "C")

    elif choice == "3":
        celsius = float(input("Enter Celsius: "))
        result = celsius_to_kelvin(celsius)
        print("Result:", round(result, 2), "K")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()