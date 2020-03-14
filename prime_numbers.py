import math

def is_prime_number(x):
    is_prime = True
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            is_prime = False
            break
    return is_prime

n = int(input())
cnt = 0
for _ in range(n):
    num = int(input())
    if is_prime_number(num):
        cnt += 1

print(cnt)