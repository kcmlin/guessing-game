########################################
# practice to create a guessing game:
# guess a number between 1 and 100
#
# Katherine Schaughency
# 17 Jan 2025
# ---------------------------------------
# Ref: "Introduction to Python" on Coursera
########################################

import random

# generate a random number between 1 and 100
randnum = random.randint(1,101)

# computer guesses
def computerguess(lowvalue, highvalue, randnum, count=0):

  # valid high and low values
  if highvalue >= lowvalue:
    
      # define how computer guesses
      # // ensure it is a whole number 
      guess = lowvalue + (highvalue - lowvalue)//2  

      if guess == randnum:
          return count

      elif guess > randnum:
          count = count + 1
          return computerguess(lowvalue, guess - 1, randnum, count)
      
      else:
          count = count + 1
          return computerguess(guess + 1, highvalue, randnum, count)

  # invalid high and low values
  else:
      return -1
#end computer guesses

# start player guesses with a while loop
count = 0 
guess = -99

while (guess != randnum):

    # enter player guess
    guess = (int)(input("Enter your guess between 1 and 100: "))

    # compare player guess with randnum
    if guess > randnum:
        print("lower")
      
    elif guess < randnum:
        print("higher")

    else:
        print("you got it!")
        break
      
    # if player does not guess it right, add the count and guess again  
    count = count + 1

# print the final results
print("it took you " + str(count) + "guesses to get it")
print("it took the computer " + str(computerguess(0,100,randnum)) + " guesses")

