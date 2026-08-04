'''A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated.'''


def number(n) :
    for i in range(1 , n + 1):
        yield i
N = int(input("enter a value of N : "))
print("Generated numbers:")
for num in number(N):
    print(num)        

