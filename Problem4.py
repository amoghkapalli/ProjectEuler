'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

from math import ceil
first_num=100
max_product=0
def palindrome_checker(num):
   s=str(num)
   first_frag=s[0: len(s)/2]
   second_frag=s[int(ceil(len(s)/2.0)):]
   return first_frag == second_frag[::-1]
for x in range(100, 1000):
   for y in range(100, 1000):
      z=x*y
      if palindrome_checker(z):
         if z>max_product:
            max_product=z
print max_product