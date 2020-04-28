'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''
import time
import math
start_time = time.time()
amicable_nums_vals = set()
def sum_div(num):
    sum_val = 1
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            sum_val += x
            divisor = num / x
            if divisor > x:
                sum_val += divisor
    return sum_val
for first in range(1, 10000):
    for second in range(first+1, 10000):
        if sum_div(first) == second and sum_div(second) == first:
            amicable_nums_vals.update([first, second])
print(sum(amicable_nums_vals))
print("--- %s seconds ---" % (time.time() - start_time))