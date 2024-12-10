####################################################
##########  Rock Paper Scissors Game  ##############
##########  100 Days of Code - Day 4  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script greets the player and then in the   #
#  console, the player is asked to choose rock,    #
#  paper, or scissors. The selections for each     #
#  choice are assigned to an integer in the based  #
#  on the index of the choice in the list. Rock is #
#  at index 0, Paper is at 1, and Scissors is 2.   #
#  The randint method automatically handles the    #
#  pseudorandom selection of the computer. The     #
#  below script handles the logic of the game with #
#  several if else statements. When the player     #
#  and computer make their choices, the console    #
#  will output their selection rather than the     #
#  index assignment along with some fun ascii art! #
####################################################

##################  Variables  #####################
import random

rock = '''

Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Choose 0 for Rock, 1 for Scissors, and 2 for Paper.\n"))
print("You chose:")
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

###################  Script  #######################

if user_choice == 0 and computer_choice == 0:
    print("It's a draw! Try again!")
elif user_choice == 0 and computer_choice == 1:
    print("The computer won this round!")
elif user_choice == 0 and computer_choice == 2:
    print("You won this round!")
elif user_choice == 1 and computer_choice == 0:
    print("You won this round!")
elif user_choice == 1 and computer_choice == 1:
    print("It's a draw! Try again!")
elif user_choice == 1 and computer_choice == 2:
    print("The computer won this round!")
elif user_choice == 2 and computer_choice == 0:
    print("The computer won this round!")
elif user_choice == 2 and computer_choice == 1:
    print("You won this round!")
elif user_choice == 2 and computer_choice == 2:
    print("It's a draw! Try again!")