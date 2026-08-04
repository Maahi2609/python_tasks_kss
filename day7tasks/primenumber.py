'''Write a program to check whether a number is Prime'''


n = int(input("enter a num : "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print(n, "is a Prime number.")
else:
    print(n, "is not a Prime number.")
