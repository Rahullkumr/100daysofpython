import random

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

win = '''
                                 _         
                                (_)        
  _   _  ___  _   _  __      __  _   _ __  
 | | | |/ _ \\| | | | \\ \\ /\\ / / | | | '_ \\ 
 | |_| | (_) | |_| |  \ V  V /  | | | | | |
  \\__, |\\___/ \\__,_|   \\_/\\_/   |_| |_| |_|
   __/ |                                   
  |___/                                    

'''
lose = '''
                       _                
 _   _  ___  _   _    | | ___  ___  ___ 
| | | |/ _ \| | | |   | |/ _ \\/ __|/ _ \\
| |_| | (_) | |_| |   | | (_) \\__ \\  __/
 \__, |\___/ \__,_|   |_|\\___/|___/\\___|
 |___/                                 
'''
draw = '''
     _                           
    | |                          
  __| |  _ __    __ _  __      __
 / _` | | '__|  / _` | \ \ /\ / /
| (_| | | |    | (_| |  \ V  V / 
 \__,_| |_|     \__,_|   \_/\_/  
                                 
                                 
'''

#Write your code below this line 👇
'''
RULES:
  Rock(0) wins against scissors(2); 
  paper(1) wins against rock(0); 
  scissors(2) wins against paper(1).
'''
game_images = [rock, paper, scissors]

user_choice = input(
  "What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)

if int(user_choice) >= 3 or int(user_choice) < 0:
  print("\nYou typed an invalid number, You loose!")
else:
  print(game_images[int(user_choice)])
  print("\nComputer chose:")
  print(game_images[computer_choice])

  if int(user_choice) == 0 and computer_choice == 2:
    print(win)
  elif int(user_choice) == 2 and computer_choice == 0:
    print(lose)
  elif int(user_choice) < computer_choice:
    print(lose)
  elif int(user_choice) > computer_choice:
    print(win)
  elif computer_choice == int(user_choice):
    print(draw)
