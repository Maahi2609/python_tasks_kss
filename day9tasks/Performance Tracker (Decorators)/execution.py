'''A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.'''



import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()          
        result = func(*args, **kwargs)
        end = time.time()            

        print(f"Execution Time: {end - start:.23f} seconds")
        return result
    return wrapper

@execution_time
def process_data():
    print("Processing data...")
    time.sleep(6)
    print("Processing complete.")


process_data()