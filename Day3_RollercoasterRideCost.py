####################################################
########  Rollercoaster Price Calculator  ##########
##########  100 Days of Code - Day 3  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script utilizes if else statements to      #
#  determine if a customer is able to ride the     #
#  rollercoaster. This is determined first by the  #
#  rider's height. If their height in inches       # 
#  doesn't meet the minimum required height, the   # 
#  script exits with a print statement telling     #
#  customer that they're not tall enough to ride,  #
#  otherwise the script goes through a set of if   #
#  else statements and if they meet one of the     #
#  defined conditional statements, the script      #
#  will then determine their cost to ride and      #
#  then will ask if they wish to take a photo for  #
#  an additional cost. When the script finishes,   #
#  their final cost will output in the console.    #
####################################################

# todo: work out if the customer can ride based on 
# their height and then determine the cost based upon 
# their age and choice of if they want to take a photo.

##################  Variables  #####################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
bill = 0

###################  Script  #######################

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    elif age >= 45:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you are not tall enough to ride.")
