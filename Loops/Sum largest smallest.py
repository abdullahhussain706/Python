cmd = "quit"
total = 0
smallest = largest = None
count = 0
while True:
    number = input("Enter Number: ")
    if number == cmd:
        break
    number = int(number)
    count += 1
    total += number
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number
if count > 0:
    print(f"Total {total} \t Smallest is: {smallest} \t Largest is: {largest}")
else:
    print("No Number Entered.")
