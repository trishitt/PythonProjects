print ( ''''             
                    o___.-' /
                    |      _\_
                    |___.-'   `
                    |
                    |
            _   _   j   _   _
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
  _   _   _  [_j__j__j__j__]  _   _   _   _
_[_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
  _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
     j  j  j [  j  j  j  j ] j  j  j  j    \n''''')

print('Welcome to the infamous treasure island! Live or Die!\n')

print ('Here you will get out or you will be dead as per your choices you make!\nTreasure will be your LIFE!\n')

choice1 = input('You are at a cross road. WHere do you want to go?\n Two Choices => Left or Right \n')

if choice1 == 'Left':
  print('\nYou have come to a lake. There is an island in the lake.\n ')
  choice2 = input("Type 'Wait' for a boat or 'Swim' to swim accross\n")
  if choice2 == 'Wait':
    print('\nYou arrived at the island succesfully.\nThere are 3 doors to live your live richly.\n1 will be making you rich, other 2 will kill you. choose!\n')
  
    choice3 = input('Choose one door=> Red, Blue, Yellow\n')
    if choice3 == 'Yellow':
      print('\nWoohhooooo! You won! You are the richest person in the world to live now!')
    else:
      print('You lost. You entered the beast room. Better Luck next time!!')

  else:
    print('Uh-Oh! Crocodiles ate you! You are dead!')
else:
    print('Whoops its a trap door to dungeons! You are dead!')
    print("""_                       _                  
| |                     | |                 
| |_ _ __ __ _ _ __   __| | ___   ___  _ __ 
| __| '__/ _` | '_ \ / _` |/ _ \ / _ \| '__|
| |_| | | (_| | |_) | (_| | (_) | (_) | |   
 \__|_|  \__,_| .__/ \__,_|\___/ \___/|_|   
              | |                           
              |_|                           """)
