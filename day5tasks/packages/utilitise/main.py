from utilitise.math_operations import add, multiply
from utilitise.string_operations import to_uppercase, count_characters
a = int(input("enter a num : "))
b = int(input("enter a num : "))
print("addition : ", add(a, b))
print("multiplication : ", multiply(a, b))
text = input("enter a string : ")
print("upper case : ", to_uppercase(text))
print("characters count : ", count_characters(text))