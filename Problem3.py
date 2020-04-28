'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

from math import sqrt

def determine_factor(num):
   factors = []
   if num ==2:
      factors.append(2)
      return factors
   #for loop to find the prime numbers and skips over the even numbers with the stride of 2
   for i in xrange(3, int(sqrt(num)), 2):
      if num % i == 0:
         #to check if its prime recursion is used to find the 
         if len(determine_factor(i))==0:
            factors.append(i)
         
   return factors

print determine_factor(600851475143)
   
      