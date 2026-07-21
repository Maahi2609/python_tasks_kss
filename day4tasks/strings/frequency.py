a = input("Enter a string: ")
frequency = {}
for ch in a:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print("Character frequencies:")
for ch in frequency:
    print(ch, ":", frequency[ch])