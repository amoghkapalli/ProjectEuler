'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?'''
import time
start_time = time.time()

def collatz_num_gen (n):
    chainNumber = 1
    changing_n = n
    while changing_n != 1:
        if changing_n % 2 == 0:
            changing_n = changing_n/2
            chainNumber += 1
        else:
            changing_n = (3*changing_n) + 1
            chainNumber += 1
    return [chainNumber, n]
        
list_of_collatz = []
for i in range(2, 1000000):
    list_of_collatz.append(collatz_num_gen(i))
sortedList = sorted(list_of_collatz, reverse=True)
print(sortedList[:1])
print("--- %s seconds ---" % (time.time() - start_time))