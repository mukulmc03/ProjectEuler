#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def LargestPrimeFactor(num):
    a = 2
    list = []
    while a <= num:
        if num % a == 0:
            b, count = 2, 0
            while b <= a:
                count += 1
            x += 1
print("Factors of a Number", LargestPrimeFactor(10))