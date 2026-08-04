'''A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects.'''

class Result:
    def calculate_result(self, sub1, sub2, sub3):
        total = sub1 + sub2 + sub3
        average = total / 3
        print("Result using 3 subjects: ")

        print("Total =", total)
        print("Average =", average)

r = Result()
r.calculate_result(23, 87, 56)
    
