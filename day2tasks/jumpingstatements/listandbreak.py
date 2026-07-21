numbers = [12, 67, 98, 1000, 131]
search = int(input("Enter a number to search: "))
for num in numbers:
    if num == search:
        print("Number found:", search)
        break
else:
    print("Number not found")