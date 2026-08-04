'''Create a generator function that continuously generates even numbers starting from
2. The program should print the first N even numbers using this generator.'''

def even_numbers():
    num = 2
    while True:
        yield num
        num += 2

N = int(input("Enter the value of N: "))
gen = even_numbers()

print("First", N, "even numbers are:")
for i in range(N):
    print(next(gen))
