"""
Assignment #8, Part 1
Andrew Park
"""

import math

#storing the value
num=0

#infinite loop until valid input

while True:
    num=int(input("Enter the value of num : "))
    if(num>=10):
        break
    else:
        print("Invalid number! At least 10.")

#create list to hold prime numbers

number = []

for i in range(num+1):
    number.insert(i,'P')

#first 2 numbers

number[0]='N'

number[1]='N'

#even numbers except 2 is N

for i in range(4,num+1,2):
    number[i]='N'

#max

max=int(math.sqrt(num))

for i in range(3,max+1,2):
    if number[i]=='P':
        for p in range(i*i,num+1,2*i):
            number[p]='N'

#prime

p=int(1)

for i in range(len(number)):
    if number[i]=='P':
        if p%10==0:
            p=1
            print('{:<5}'.format(i))
        else:
            p=p+1
        print('{:<5}'.format(i),end="")

print()
