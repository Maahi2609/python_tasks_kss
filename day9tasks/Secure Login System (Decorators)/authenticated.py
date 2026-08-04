'''A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function.'''

logged_in = False

def login_required(func):
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("Access Denied! Please log in first.")
    return wrapper

@login_required
def view_account():
    print("Welcome! You can now access your account details.")

view_account()
logged_in = True
print("\nUser logged in successfully.\n")
view_account()