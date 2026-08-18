'''Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary.'''

'''Q:Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary'''
users = {"Mahesh": "admin","Loki": "user","Jaggu": "manager"}
def check_role(required_role):
    def decorator(func):
        def wrapper(username):
            if users.get(username) == required_role:
                return func(username)
            else:
                print("Access denied for", username)
 
        return wrapper
    return decorator
@check_role("admin")
def delete_data(username):
    print(username, "can delete data")
@check_role("manager")
def view_reports(username):
    print(username, "can view reports")
@check_role("admin")
def add_user(username):
    print(username, "can add users")
delete_data("Mahesh")
delete_data("Loki")
view_reports("Jaggu")
view_reports("Mahesh")
add_user("Mahesh")
 

   