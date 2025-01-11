import os
os.system('cls')

num = int(input('Enter Size for Rigt Triangle: '))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print("*", end='')
        j = j+1
    print()
    i = i+1
