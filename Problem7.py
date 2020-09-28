# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime
# is 13.
# What is the 10001st prime number?

from math import sqrt

num = 1
count = 0
N = 0


def prime(n):
    sqroot = int(sqrt(n))
    j = 2
    while j <= sqroot:
        if n % j == 0:
            return False
        j = j + 1
    return True


N = 10001
while (True):
    num = num + 1
    if prime(num):
        count = count + 1
    if count == N:
        print(count, 'th prime is ', num)
        break


