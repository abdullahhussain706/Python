import os
os.system('cls')

i = 0
number = int(input("Enter the Limit for Armstrong Numbers: "))
while i <= number:
    number_str = str(i)
    num_digit = len(number_str)
    sum_number = sum(int(digit)**num_digit for digit in number_str)
    if sum_number == i:
        print(f"{i} is armstrong number.")
    i += 1
