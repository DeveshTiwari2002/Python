import random as rnd
import os


def welcome():
  print("""
       _      _  ______   _        _____     _______     _    _   ______
        |    |  |         |       |         /       \    |\  /|  |
        | /\ |  |----     |       |        |         |   | \/ |  |----
        |/  \|  |______   |_____  |_____    \_______/    |    |  |______
  """)
  user_input = int(input('Enter 1 to play, 0 to exit: '))

  if user_input == 1:
    print('   ')
    print('                   You have only 5 chance to win the game.')
    print('  ')
    user_try(computers_guess())
  else:
    exit()


def computers_guess():
  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  return rnd.choice(list)


def user_try(cg):
  x = 0
  while (x != 5):
    x += 1

    ug = int(input('Enter ' + str(x) + ' Try! --> '))

    if ug == cg:
      print('Great')
      break
    if ug > cg:
      if x < 5:
        print('Try again! Your guess is greater.')

    if ug < cg:
      if x < 5:
        print('Try again! Your guess is smaller.')

    if x == 5:
      print('You are terminated')
      os.system('clear')
      welcome()
welcome()






