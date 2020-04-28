'''Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

from math import ceil
def prime_checker(num):
    top=ceil(num ** .5)+1
    #checks primes from 3 while skipping the even numbers
    for x in range (3, top , 2):
        if num % x ==0:
            return False
    return True


def primes(max=10):
    yield 2
    found=1
    current=3
    while found<max:
        if prime_checker(current):
            yield current
            found+=1
        current+=2

for prime in primes(10001):
    print(prime)
