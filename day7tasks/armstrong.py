'''Write a program to check whether a given number is an Armstrong number or not.
'''

n = int(input("enter a number : "))
x = len(str())
temp = n
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r**x
    n = n//10
if(temp == sum):
    print("Armstrong number : ")
else:
    print("Not an Armstrong number : ")        
