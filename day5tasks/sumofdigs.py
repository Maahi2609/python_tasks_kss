def sum_of_digits(n):
    if n == 0:     
        return 0
    return (n % 5) + sum_of_digits(n // 5)
print(sum_of_digits(362))