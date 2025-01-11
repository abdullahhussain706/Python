import os
os.system('cls')

num = int(input('Enter Size for Rigt Triangle: '))
i = 1
while i <= num:
    a = 1
    while a <= num-i:
        print(" ", end='')  # ens function prevent cursor to newline
        a += 1
    j = 1
    while j <= i:
        print("*", end='')
        j += 1
    print()
    i += 1
