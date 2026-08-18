'''Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling
'''
try:
    with open("user_logs.txt", "a") as file:

        while True:
            action = input("Enter user action (or type 'exit' to stop): ")

            if action.lower() == "exit":
                break

            file.write(action + "\n")
            print("Action logged successfully.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)
print("Logging completed.")