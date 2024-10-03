import random
import math
#taking Inputs
lower=int(input("Enter Lower Bound: "))#5
#taking Inputs
upper=int(input("Enter upper Bound: "))#20

# generating random number between
# the lower and upper
x=random.randint(lower,upper)

print('\n\You have only',round(math.log(upper-lower+1,2))," chances to guess the integer!\n")

# Initializing the number of guesses.
count=0

# for calculation of minimum number of
while count < math.log(upper-lower+1,2):
    count+=1

# taking guessing number as input
    guess = int(input("Guess a number:- "))

#condition testing
    if x==guess:
        print("Congratulations you did it in ",
              count, " try")
    #once gussed,loop will break
        break
    elif x> guess:
        print("you guessed too small!")
    elif x<guess:
        print("you guess too high!")

# If Guessing is more than required guesses,
# shows this output.

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")


  