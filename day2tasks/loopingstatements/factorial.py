Z = int(input("Enter a number: "))
factorial = 1
for i in range(1, Z + 1):
    factorial = factorial * i
print("Factorial of", Z , "is:", factorial)