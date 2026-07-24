def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [16, 89,76,3,17]
result = find_sum(numbers)
print("Sum of the elements:", result)