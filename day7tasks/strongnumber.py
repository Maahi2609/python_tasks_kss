'''Write a program to check whether a given number is a Strong number'''


n = int(input("enter a number : "))
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    n = temp % 10
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    sum = sum + fact
    temp = temp // 10
if sum == num:
    print(num, "is a Strong number.")
else:
    print(num, "is not a Strong number.")