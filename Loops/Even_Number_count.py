start_value = int(input("Enter Starting Point for Even Numbers: "))
end_value = int(input("Enter End Point for Even Numbers: "))
count = 0
for i in range(start_value, end_value):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} Even Numbers")
