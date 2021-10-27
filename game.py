# libraries- collection of std codes...
# module is a collection of pre-build functions...
# package is the software "repository"...

import random

# lets see how many chances the computer need to guess the number...
def computer_chance(lower_v,higher_v,rand_num,count=0):
    if higher_v >= lower_v:
        # divide and conquer approach...
        guess = lower_v + (higher_v-lower_v)//2
        if guess == rand_num:
            return count
        elif guess > rand_num:
            # this means number in lower half...
            count=count+1
            return computer_chance(lower_v,guess-1,rand_num,count)
        else:
            count=count+1
            return computer_chance(guess+1,higher_v,rand_num,count)
    else:
        return -1

# generate a random number...
rand_num = random.randint(1,100)
# print(rand_num)           # This is to check the number in case the code is need to be verified...

count=0
guess=-99

while(guess!=rand_num):
    guess = (int)(input("Enter your guess between 1 and 100:"))
    if guess < rand_num:
        print("Higher")
    elif guess > rand_num:
        print("Lower")
    else:
        print("you guessed it...")
        break
    count=count+1

print("You took "+str(count)+" steps to guess the number correctly.")

print("Computer took "+ str(computer_chance(0,100,rand_num))+ " steps to reach")


