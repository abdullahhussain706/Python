import os
os.system('cls')

i = 2


number = int(input("Enter the Limit for Perfect Numbers: "))
while i <= number:
    j = 1
    sum_divisors = 0
    while j <= i // 2:  # divisors of number never greater than half of number
        if i % j == 0:
            sum_divisors += j
        j += 1
    if sum_divisors == i:
        print(i)
    i += 1
