'''data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers.
'''

data = [[1, 2, 3], [4, 5], [6]]
flat_list = [num for sublist in data for num in sublist]
print("Flattened list:", flat_list)
even_squares = [num ** 2 for num in flat_list if num % 2 == 0]
print("Even squares:", even_squares)