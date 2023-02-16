def take_user_input():
    number1 = int(input('Enter a number 1: '))
    number2 = int(input('Enter a number 2: '))

    user_input = {'num1': number1, 'num2': number2}

    return user_input


def mathematical_calculator(number1, number2):
    print(number1 + number2)
    print(number1 - number2)


userNum = take_user_input()

mathematical_calculator(userNum['num1'], userNum['num2'])
