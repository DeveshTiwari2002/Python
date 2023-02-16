def take_attendance():
    student1 = int(input('Enter total attendance of S1: '))
    student2 = int(input('Enter total attendance of S2: '))

    attendance = {'std1': student1, 'std2': student2}

    return attendance


def check_eligibility(student1, student2):
    if student1>75:
        print('Student1 is eligible for mid sem!')
    else:
        print('Student1 is not eligible for mid sem!')
    if student2>75:
        print('Student2 is eligible for mid sem!')
    else:
        print('Student2 is not eligible for mid sem')
userInput = take_attendance()

check_eligibility(userInput['std1'], userInput['std2'])