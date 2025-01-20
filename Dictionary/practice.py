# birthdays in dictionary parctice

import os
os.system('cls')

birthdays = {'ali': 'Apr 1', 'zilal': 'Dec 5', 'zain': 'Mar 15'}

while True:
    name = input('Enter Name: (Blank to quit): ')
    name.upper()
    if name == '':
        break
    if name in birthdays:
        print(f'{birthdays[name]} + is birthday of + {name}')
    else:
        print(f"I don't have birthday information of {name}.")
        bday = input('What is their Birthday: ')
        birthdays[name] = bday
        print('Birthday database updated.')
        print(birthdays)
