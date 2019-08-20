from __future__ import absolute_import, print_function
import os
import sys
import time

from test_celery.celery import app

@app.task
def longtime_add(x, y):
        print('>longtime_add')
        # sleep 5 seconds
        time.sleep(5)
        print('<longtime_add')
        return x + y

@app.task
def fibonacci(n): 
    print('>fibonacci')
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        #print('<fibonacci')
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        #print('<fibonacci')
        return 1
    else: 
        print('<fibonacci')
        return fibonacci(n-1)+fibonacci(n-2) 

@app.task
def find_primes(n):
    print('>find_primes')
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    print("<find_primes")
    return n

@app.task
def prime_factors(n):
    print('>prime_factors')
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print('<prime_factors')
    return factors
