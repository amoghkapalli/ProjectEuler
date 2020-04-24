'''The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?'''

import time
start_time = time.time()
def collatz_chain_generator(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count


def return_n_with_longest_chain(m):
    n = 1
    chain_count = 0
    while n < m:
        ccg = collatz_chain_generator(n)
        if ccg > chain_count:
            chain_count = ccg
            position = n
        n += 1
    return position

print(return_n_with_longest_chain(1000000))
print("--- %s seconds ---" % (time.time() - start_time))