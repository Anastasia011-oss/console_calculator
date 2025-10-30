def main():
    print("=== Console Calculator ===")

    while True:
        try:
            print("\n--- MENU ---")
            print("1 - Addition (+)")
            print("2 - Subtraction (-)")
            print("3 - Multiplication (*)")
            print("4 - Division (/)")
            print("0 - Exit")

            choice = input("Choose an option: ").strip()

            if choice == '0':
                print("Exiting the calculator.")
                break

            if choice == '1':  # Addition
                num1_input = input("Enter the first number: ").strip()
                num1 = float(num1_input)

                num2_input = input("Enter the second number: ").strip()
                num2 = float(num2_input)

                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")

        except ValueError:
            print("Error: please enter valid numbers!")


if __name__ == "__main__":
    main()

    main()

