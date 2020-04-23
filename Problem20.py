'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!'''

from math import factorial
factorial_val=factorial(100)
digi_checker=str(factorial_val)
len_digi_Checker=len(digi_checker)
sum_digits=0
for i in range (len_digi_Checker):
    sum_digits+=int(digi_checker[i])
print(sum_digits)
