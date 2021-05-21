cdef extern form "fib.h"
    long int fib(int n)

def fibonacci(n):
    return fib(n)
