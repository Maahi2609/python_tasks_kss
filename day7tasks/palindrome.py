'''Write a program to check whether a number is a Palindrome.'''

num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    n = temp % 10
    reverse = reverse * 10 + n
    temp = temp // 10
if reverse == num:
    print(num, "is a Palindrome number.")
else:
    print(num, "is not a Palindrome number.")