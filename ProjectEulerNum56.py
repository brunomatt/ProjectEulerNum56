##A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

##Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time, math
start = time.time()

max_sum = 0
naturals = [a for a in range(1,100)]

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

for a in naturals:
    for b in naturals:
        digit_sum = sum(deconstruct(pow(a,b)))
        if digit_sum > max_sum:
            max_sum = digit_sum

print(max_sum)

stop = time.time()
print("Time: ", stop - start)