import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ['trishit','srimonti', 'tinu', 'pakhi', 'potka', 'piya', 'uditi','adriksh' ]
random_word = random.choice(words)

length = len(random_word)

print(random_word)
print(length)

life = 6

display = []

for length in range (0, length):
   display += '_'
print(display)

end_of_game = False

while not end_of_game:
    Guess = input('Guess a word of the letter to get started. \n').lower()

    for position in range (0, length+1):
        letter = random_word[position]
        if letter == Guess:
            display[position] = Guess
            
    print(display)

    if Guess not in random_word:
        life -= 1
        if life == 0:
            end_of_game = True
            print ('you Lost')

    if '_' not in display:
        end_of_game = True
        print ('You Won')
    
    print (stages[life])
