"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def fib(x):
    if x <= 1:
        return x
    return fib(x-1)+fib(x-2)

def get_fib(position):
    return fib(position)