#!/usr/bin/env python3
import time
import functools

def timeit(func):
    """Decorator to measure execution time of a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timeit
def calculate_sum(n):
    """Example function to test timeit"""
    return sum(range(n))
