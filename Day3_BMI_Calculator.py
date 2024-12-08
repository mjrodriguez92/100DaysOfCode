####################################################
################  BMI Calculator  ##################
##########  100 Days of Code - Day 3  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script takes the values assigned to the    #
#  weght and height variables and uses the integer #
#  values assigned to these to calculate a         #
#  person's BMI.                                   #
#                                                  #
####################################################

##################  Variables  #####################

weight = 85
height = 1.85

bmi = weight / (height ** 2)

###################  Script  #######################

if bmi < 18.5:
    print("underweight")
elif bmi <= 18.5:
    print("normal weight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")