'''Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.'''

from math import ceil

def prime_checker(num):
    if num==2:
        return True
    elif num % 2==0:
        return False
    top=ceil(num ** .5)+1
    #checks primes from 3 while skipping the even numbers
    for x in range (3, top, 2):
        if num % x ==0:
            return False
    return True
# print(prime_checker(17))
def quadratic_primes(x_con, c_con):
    n=0
    quad = abs(n**2 + (x_con*n) + c_con)
    quad_checker=prime_checker(quad)
    while quad_checker:
        yield quad
        n+=1
        quad=abs(n**2 + (x_con*n) + (c_con))
        quad_checker=prime_checker(quad)
if __name__ == '__main__':
    current_longest=(1, 41, len([quad_checker for quad_checker in quadratic_primes(1, 41)]))
    for x_con in range(-999, 1000):
        #if not prime_checker(a):
         #   continue
        for c_con in range(-1000, 1001):
          #  if not prime_checker(b):
          #      continue
            primes= [quad_checker for quad_checker in quadratic_primes(x_con, c_con)]
            if len(primes) > current_longest[2]:
                current_longest = (x_con, c_con, len(primes))

    print(current_longest[0]*current_longest[1])



