'''A user wants to save grocery items in a file grocery.txt. Write a Python program that
takes multiple items from the user and writes them into the file, with each item on a
new line.'''

n = int(input("enter no of grocery items : "))
with open("grocery.txt","w") as file :
    for i in range(n):
        item = input(f"enter item {i + 1} : ")
        file.write(item + "\n")
        print("grocery items saved")