import os
os.system('cls')

a = 0
b = 1
number = int(input("Enter Number Limit for Fabonacci Series: "))
if number > 0:
    print(a)
if number >= 1:
    print(b)
while True:
    sequence = a + b
    if sequence >= number:
        break
    print(sequence)
    a = b
    b = sequence
