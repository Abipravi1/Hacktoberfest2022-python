import random
import time

print('Welcome to Guess The Number game!')
time.sleep(3)
print('What difficulty would you like to play in?')
time.sleep(1)
print('\n')
print('1 for Very Easy')
print('2 for Easy')
print('3 for Moderate')
print('4 for Hard')
print('5 for Very Hard')
print('6 for Impossible')
print('\n')
while True:
    diff = int(input('Enter Difficulty: '))
    print('\n')
    print('Type a random number and we will tell if your number is higher or lower than the number you have to guess')
    print('\n')
    if diff == 1:
        x = random.randint(0, 10)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You Won!')
                time.sleep(2)
                break
    if diff == 2:
        x = random.randint(0, 50)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You Won!')
                time.sleep(2)
                break
    if diff == 3:
        x = random.randint(0, 100)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You Won!')
                time.sleep(2)
                break
    if diff == 4:
        x = random.randint(0, 500)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You just beat the hard level!')
                time.sleep(2)
                break
    if diff == 5:
        x = random.randint(0, 1000)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You just beat the very hard level!')
                time.sleep(2)
                break
    if diff == 6:
        x = random.randint(0, 10000)
        while True:
            y = int(input('Enter your number: '))
            if y > x:
                print('Your number is bigger')
            elif x > y:
                print('Your number is smaller')
            elif y == x:
                print('Congratulations, You just beat the impossible level!')
                time.sleep(2)
                break
    print('Would you like to continue (Yes or No)')
    z = input().lower()
    if z == 'yes':
        continue
    elif z == 'no':
        print('\n')
        print('Thanks for playing this game!')
        break
