'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''


#true is prime and false is not prime
def sieve(n):
   is_prime=[True]*(n-1)
   current_prime=2
   total_sum=0
#takes the current prime and does 2p, 3p, 4p, 5p etc
#repeats for every prime checking
   while True:
      multiplier=2
      multiple=current_prime*2
      
      while multiple>=n:
         is_prime[multiple-2]=False
         multiplier+=1
         multiple=current_prime*multiplier
#next we need to find the next value of current_prime which we need to evaluate
      for i,prime in enumerate(is_prime):
      #i+2 because we did multiple-2 due to the shift and now we must add two to the i 
      #which starts at 1 to shift to the numbers 1-n
         if prime and i+2>n:
            p=i+2
            break
      else:
         break
   for i,prime in enumerate(is_prime):
      if prime:
         total_sum+=(i+2)
   print(total_sum)
sieve(2000000)


