'''Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates
'''
import random
numbers = []
for i in range(10) :
    a = random.randint(1, 100)
    numbers.append(a)
print("numbers : ",numbers) 

even = 0
odd = 0
for num in numbers :
    if num % 2 == 0 :
        even += 1
    else :
        odd += 1
print("Even numbers : ", even)
print("Odd numbers : ", odd)
unique_numbers = set(numbers)
print("after removing duplicates : ",unique_numbers)