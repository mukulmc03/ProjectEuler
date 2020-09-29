# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a ^ 2 + b ^ 2 = c ^ 2
# For example, 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 5 ^ 2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 0
b = 0
c = 0
s = 1000

found = False
for a in range(1, s // 3):
    for b in range(a, s // 2):
        c = s - a - b
        if  a * a + b * b == c * c:
            found = True
            break
    if found:
        break

print(a * b * c)