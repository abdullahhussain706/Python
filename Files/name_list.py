# list text file

import os 
os.system('cls')

with open("names.txt", "w") as file:
    file.write("Abdullah Zarwan Rizwan")


with open("names.txt", "r") as file:
    content=file.read()
    print(f"Data in file:  {content}")