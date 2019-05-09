def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0


print(power_of_two())
print(power_of_two())
