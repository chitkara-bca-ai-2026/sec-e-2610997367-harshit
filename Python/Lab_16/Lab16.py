import math

history = []

def box(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

box('ENTERPRISE MODULAR UTILITY CALCUATOR')

while True:
    print('Select an operation:\n')
    print('1. Addition (+)\n 2. Subtraction (-)\n 3. Multiplication\n 4. Division (/)\n 5. Modulas / Remainder (%)\n 6. Power / Exponentiation (Default: Square)\n 7. View Calculation History\n 8. Exit\n ')
    choice = int(input('Enter your choice (1-8): '))
    if choice == 8:
        print("\nAlright. Bye.")
        break
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    if choice == 1:
        add = first_number +  second_number
        print(f"\n[RESULT] {first_number} + {second_number} = {add}")
    if choice == 2:
        sub = first_number - second_number
        print(f"\n[RESULT] {first_number} - {second_number} = {sub}")
    if choice == 3:
        mul = first_number * second_number
        print(f"\n[RESULT] {first_number} * {second_number} = {mul}")
    if choice == 4:
        div = first_number / second_number
        print(f"\n[RESULT] {first_number} / {second_number} = {div}")
    if choice == 5:
        mod = first_number % second_number
        print(f"\n[RESULT] {first_number} % {second_number} = {mod}")
    if choice == 6:
        expo = math.pow(first_number, second_number)
        print(f"\n[RESULT] {first_number} Expo {second_number} = {expo}")
    if choice == "7":
        print("\n--- Calculation History ---")
        if history:
            for number, record in enumerate(history, start=1):
                print(f"{number}. {record}")
        else:
            print("No calculations yet.")
        continue