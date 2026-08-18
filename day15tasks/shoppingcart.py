'''Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except
'''

try :
    lu = ([10, 29, 77, 54, 29, 45])
    unique_numbers = set(lu)
    

    total = 0

    for i in unique_numbers :
     if i > 0 :
        total += 1

    print("unique items : ",unique_numbers)
    print("total cost : ", total)
except(ValueError, TypeError) :
   print("Invalid input")   