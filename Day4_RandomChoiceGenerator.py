####################################################
##############  Find The Treasure  #################
##########  100 Days of Code - Day 3  ##############
####################################################

####################################################
################  Description  #####################
#                                                  #
#  This takes a list of random friends and below   #
#  in the script is two versions of a pseudo       #
#  random generator to pick a random person from   #
#  the list. The first option uses a the random    #
#  choice method and the second uses the randint   #
#  method with a number index to define which of   #
#  the friends in the list to choose at random.    #
#  The first option uses all of the friends and    #
#  the second is restricted to a specific index.   #
####################################################

##################  Variables  #####################

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

###################  Script  #######################

# 1st option
print(random.choice(friends))

# 2nd option
random_index = random.randint(0, 4)
print(friends[random_index])