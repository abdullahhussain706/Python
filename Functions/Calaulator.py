# function in fuction paractice and make calculator

import os
os.system('cls')


# def operation(a, b, operater):
#     return operater(a, b)
def operation(a, b, operator): return operator(a, b)


def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b
def pow(a, b): return a**b


print('''
      1 for Addition
      2 for Subtraction
      3 for Multiplication
      4 for Division
      5 for Power
      ''')
a = input("Enter Your Choice: ")
b = int(input('Enter First Number: '))
c = int(input('Enter Second Number: '))

if a == '1':
    print(f'Addition={operation(b, c, add)}')
elif a == '2':
    print(f'Subtraction={operation(b, c, sub)}')
elif a == '3':
    print(f'Multiplication={operation(b, c, mul)}')
elif a == '4':
    print(f'Division={operation(b, c, div)}')
elif a == '5':
    print(f'Power={operation(b, c, pow)}')
else:
    print("Invalid Choice!")
