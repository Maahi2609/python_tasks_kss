li = [10,20,30,40,50,10,20,60]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
        print("original list : ",li)
        print("list after removing duplicates : ",unique)