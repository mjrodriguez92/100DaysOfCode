####################################################
#########  Heads or Tails Randomization  ###########
##########  100 Days of Code - Day 4  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This script utilized the random python module   #
#  to facilitate a heads or tails program. The     #
#  values for heads and tails are assigned to as   #
#  as a 0 (heads) value or 1 (tails). through the  #
#  the use of randomization, if else statements    #
#  are then used to output heads or tails to the   #
#  console based upon whether the numbers 0 or 1   #
#  are randomly generated when the program is run. #
####################################################

##################  Variables  ######################

import random
random_heads_or_tails = randint(0, 1)

###################  Script  #######################

if random_heads_or_tails == 0:
   print("Heads")
elif random_heads_or_tails == 1:
   print("Tails")