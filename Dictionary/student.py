
import os
os .system('cls')

student = {
    "name": "John Doe",
    "age": 18,
    "grade": "A"
}
print("Student Name:", student["name"])
student["favorite_subject"] = "Mathematics"     # add a key pair value
student["grade"] = 'A+'       # update a value
print(student)
del student["favorite_subject"]
print(student)

print("Values in student:")
for i in student.values():
    print(i, "  ", end='')

print('\nKeys in Student: ')
for j in student.keys():
    print(j, "  ", end='')

print('\nData in Student:')
for k in student.items():
    print(k, "  ", end='')


print(list(student.values()))
