####################################################
##########  Restaurant Tip Calculator  #############
##########  100 Days of Code - Day 2  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script greets the user and then begins     #
#  to query for how much the total bill is and     #
#  records the value as a floating integer. The    #
#  console then queries for the percentage to      #
#  tip the server and stores this values as an     #
#  integer. Lasltly the console requests for how   #
#  many people are paying the bill to equally      #
#  split the cost between everyone and stores      #
#  this also as an integer. The following          #
#  variables perform conversions to ensure the     #
#  tip is evaluated as a percentage of the bill,   #
#  the final bill includes the subtotal plus the   #
#  total tipped, and the last evaluation           #
#  calculates how much each person pays toward     #
#  the final bill to achieve the correct amount.   #
####################################################

###################  Script  #######################

print("Welcome to the tip calculator!")
##################  Variables  #####################
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")

