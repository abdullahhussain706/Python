import os
import random

os.system('cls')

print('Think Number Between 1 to 20')
attempt = 0
target = random.randint(1, 20)

while True:
    num = int(input('Make a guess: '))
    attempt += 1

    if num < target:
        print("Your Guess is too low.")
    elif num > target:
        print('your guess is too high.')
    else:
        print('Congratulations!')

    if attempt == 3:
        break
print('Try Again!')
