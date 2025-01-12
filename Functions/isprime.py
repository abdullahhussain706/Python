# for check number is prime or not

import os
os.system('cls')


def isprime(num):
    if num < 1:
        return False
    else:
        a = 0
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


a = int(input('Enter Number for checking Prime: '))
print(isprime(a))
