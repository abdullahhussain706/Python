import os
os.system('cls')

fruits = ['Apple', 'Mango', 'Pineapple', 'Lemon', 'Cherry']
print(fruits)       # print full list

print(fruits[2])        # print 3rd element in list
print(fruits[-1])       # print last
print(fruits[:2])       # print from start to index 2
fruits[1] = 'Amrood'      # change index 1 mango with amrood
print(fruits)
print(f'Length of list: {len(fruits)}')     # findd length of list
fruits = fruits+['Orange']      # concatenate list
print(fruits)
