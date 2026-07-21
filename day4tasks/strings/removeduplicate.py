z = input("Enter a string: ")
result = ""
for ch in z:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)