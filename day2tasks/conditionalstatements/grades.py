marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "X"
elif marks >= 75:
    grade = "Y"
elif marks >= 50:
    grade = "Z"
else:
    grade = "Fail"
print("Grade:", grade)