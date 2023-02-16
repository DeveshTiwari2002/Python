print('Welcome to Aero India')
def jet_speed():
    jet1 = float(input('Enter Jet Speed to check the qualification: '))

    return jet1


def check_qualification(jet1):
    if jet1 > 1.7:
       print('Congrats! Buckle up for some action')
    else:
        print('Too slow')

userSpeed = jet_speed()

check_qualification(userSpeed)
