import os
os.system('cls')

num = int(input("Enter Number for Factorial: "))

a = 1
factorial = 1
while a <= num:
    factorial *= a
    a += 1

print(f"Factorial is= {factorial}")
