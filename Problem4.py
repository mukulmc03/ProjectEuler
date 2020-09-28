#A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


num = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > num:
            s = str(a * b)
            if s == s[::-1]:
                num = a * b
print(num)
