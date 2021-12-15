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

print ('Welcome to RPS Association Champion!')

counter1 = 0
counter2 = 0
i = 0
while (i < 6):

  you = int(input('Select 0 for Rock, 1 for paper & 2 for scissors\n'))


  game_img =[rock,paper,scissors]


  if you > 2  or you < 0:
    print ('Invalid choice!')
  else:
    print (f"Your choice {game_img[you]}")

  computer = random.randint(0,2)
  print (f"Computer's choice {game_img[computer]}")

  
  if you == 0 and computer == 2:
      print('You Win!')
      counter1 = counter1 + 1
  elif computer == 0 and you == 2:
      print ('You Lost!')
      counter2 = counter2 + 1
  elif you > computer:
      print ('You Win!')
      counter1 = counter1 + 1
  elif computer > you:
    print ('You Lost!')
    counter2 = counter2 + 1
  elif you == computer:
    print ('DRAW!')

  print (f"Your score {counter1}")
  print (f"Computer score {counter2}")

  i += 1
