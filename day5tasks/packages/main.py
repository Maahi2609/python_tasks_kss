from utilitise import mathoperations
from utilitise import stringoperations
a = int(input("enter a num : "))
b = int(input("enter a num : "))
print("addition : ", mathoperations.add(a, b))
print("multiplication : ", mathoperations.multiply(a, b))
text = input("enter a string : ")
print("upper case : ", stringoperations.to_upper(text))
print("characters count : ", stringoperations.count_characters(text))