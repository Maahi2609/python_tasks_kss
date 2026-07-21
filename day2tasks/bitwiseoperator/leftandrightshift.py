num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))
left_shift = num << shift
right_shift = num >> shift
print("Left Shift (<<):", left_shift)
print("Right Shift (>>):", right_shift)