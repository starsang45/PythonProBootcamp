rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
my_set = {rock, paper, scissors}
USER = random.choice(list(my_set))
COMPUTER = random.choice(list(my_set))
print(USER, COMPUTER)
if USER == rock and COMPUTER == scissors:
    print("You win")
elif USER == scissors and COMPUTER == paper:
    print("You win")
elif USER == paper and COMPUTER == rock:
    print("You win")
elif USER == COMPUTER:
    print("game draw")
else:
    print("computer win")

