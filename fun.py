def take_user_input():
    number1 = input('Enter a number 1: ')
    number2 = input('Enter a number 2: ')

    user_input = {'num1': number1, 'num2': number2}
    return user_input


def check_greater_num(number1, number2):
    if number1 > number2:
        print('Number 1 is greater!')
    else:
        print('Number2 is greater!')


userNum = take_user_input()
check_greater_num(userNum['num1'], userNum['num2'])