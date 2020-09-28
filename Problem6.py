# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and
# the square of the sum.

def sumofsq(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i ** 2
    return sum

def sqofsum(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    sum = sum ** 2
    return sum

def diffinsums(num):
    return sqofsum(num) - sumofsq(num)

print(diffinsums(20))

