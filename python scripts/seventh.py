'''Write a Python decorator that measures the execution time of a function and logs it. Apply this 
decorator to a function that performs a computationally expensive task.'''
import time
import logging
logging.basicConfig(level=logging.INFO)

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@time_logger
def expensive_computation(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

result = expensive_computation(1000000)
print(f"Result: {result}")

