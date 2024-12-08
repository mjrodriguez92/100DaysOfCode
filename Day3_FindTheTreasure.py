####################################################
##############  Find The Treasure  #################
##########  100 Days of Code - Day 3  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script begins with a greeting to the user  #
#  to a treasure hunt adventure. Each step of the  #
#  adventure is presented with a set of choices.   #
#  Players beware! If you make the wrong choice,   #
#  you will meet one of the many perils down the   #
#  way and that will be Game Over! Each variable   #
#  represents each part of the story and a choice  #
#  the player has to make to proceed or perish!    #
#  The choice's are evaluated using if else        #
#  conditions and will exit with a message if the  #
#  player makes it to the treasure or game over.   #
#                                                  #
####################################################

##################  Variables  #####################


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (X) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You\re at a crossroads, which direction do you wish to go, left or right?\n").lower()
choice2 = input(""""You find an alternative path, but now You\ve come up to dangerous waters, do
                you wish to swim or find another way across? yes or no?\n""").lower()
choice3 = input("""You've made it across the dangerous waters to a mysterious island
and arrive at a house with three doors. One door is red, the second yellow, and the third
is blue. Which door do you choose?\n""").lower()

###################  Script  #######################

if choice1 == "right":
    print("You\ve fallen into a hole and died. Game Over!")
elif choice1 == "left":
    print(input(choice2))

if choice2 == "yes":
    print("""You attempted to cross the waters and lost your balance in the current and
    were swallowed up by dangerous piranha""")
elif choice2 == "no":
    print(input(choice3))

if choice3 == "red":
    print("You opened the door and were swallowed up by fire. Game Over!")
elif choice3 == "yellow":
    print("You found the treasure! You win!")
elif choice3 == "blue":
    print("You open the door to a room of monsters and were eaten alive! Game over!")