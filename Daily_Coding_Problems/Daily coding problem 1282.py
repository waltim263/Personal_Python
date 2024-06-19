"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""
total = 0
n = [int(x) for x in input()]

for number in n:
    total += number
if total > 10:
    print("This number is not perfect, please choose a different number")
elif total == 10:
    print("This number is already perfect")
else:
    n.append(10-total)
    print("Your perfect number is " + str(int(''.join(map(str, n)))))
