while True:
    print()

    num_1 = input('Type a number: ')
    num_2 = input('Type another number: ')
    operator = input('Type an operator: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('You must type a number')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)

    exit = input('Would you like to exit? [Y]es or [N]o: ')
    if exit == 'Y' or exit == 'y':
        break