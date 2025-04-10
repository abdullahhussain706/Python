#reversing a string

import os 
os.system('cls')


def reverse():
    a=input("Enter string for reverse: ")
    reversed_str=""

    for i in a:
        reversed_str=i+reversed_str
    return reversed_str



print(reverse())