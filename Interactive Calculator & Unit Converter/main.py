
# Simple Calculator and Unit Converter

def calculator():
    print("\n--- Basic Calculator ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice!")


def unit_converter():
    print("\n--- Unit Converter ---")

    print("1. Kilometer to Miles")
    print("2. Miles to Kilometer")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Grams")
    print("6. Grams to Kilograms")

    choice = input("Enter your choice: ")
    value = float(input("Enter the value: "))

    if choice == "1":
        print("Miles:", value * 0.621371)

    elif choice == "2":
        print("Kilometers:", value * 1.60934)

    elif choice == "3":
        print("Fahrenheit:", (value * 9/5) + 32)

    elif choice == "4":
        print("Celsius:", (value - 32) * 5/9)

    elif choice == "5":
        print("Grams:", value * 1000)

    elif choice == "6":
        print("Kilograms:", value / 1000)

    else:
        print("Invalid choice!")


# Main Menu

while True:

    print("\n===== MAIN MENU =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        unit_converter()

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice! Try again.")
