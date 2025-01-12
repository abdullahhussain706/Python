# maximum numberr find Function
import os
os.system('cls')


def maximum(a, b, c):
    return max(a, b, c)


print("____Enter three Numbers to find maximum____")
a = input("Enter First Number: ")
b = input("Enter Second Number: ")
c = input("Enter Third Number: ")

print(f'Maximum Number= {maximum(a, b, c)}')
