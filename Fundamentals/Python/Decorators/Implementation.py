import time
from functools import wraps

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    
    return wrapper

@timer
def example_function(duration):
    """
    Example function that sleeps for the given duration (in seconds).
    """
    time.sleep(duration)

# Test the timer decorator
example_function(2)