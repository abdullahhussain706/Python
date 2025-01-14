# To find Factorial

import os
os.system('cls')


def factorial(num):
    if num == 1:
        return 1
    else:
        fac = 1
        while num >= 1:
            fac *= num
            num -= 1
        return fac


num = int(input('Enter Number for factorial: '))
print(f'Factorial= {factorial(num)}')
