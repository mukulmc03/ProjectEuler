# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt

def sumofprime(n):
    sum = 0
    for i in range(1, n):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                sum = sum + i
    print(sum)


sumofprime(200000)