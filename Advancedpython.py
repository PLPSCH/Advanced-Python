def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That wasn't a number. Try again !")

def calculate():
    print("\n--- Select Operation ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")

    choice = input("Enter your choice (1-5): ").strip()

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice! Try a number from 1 to 5 !")
        return

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == '1':
        result = num1 + num2
        operation = "Sum"
    elif choice == '2':
        result = num1 - num2
        operation = "Difference"
    elif choice == '3':
        result = num1 * num2
        operation = "Product"
    elif choice == '4':
        result = "Undefined (can't divide by zero!)" if num2 == 0 else num1 / num2
        operation = "Quotient"
    elif choice == '5':
        result = "Undefined (can't divide by zero!)" if num2 == 0 else num1 % num2
        operation = "Modulo"

    print(f"\n{operation}: {result}")

while True:
    calculate()
    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Alrighty then... go solve real-world problems now !")
        break