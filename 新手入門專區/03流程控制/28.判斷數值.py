def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())

if N % 2 == 0:
    result = "even"
else:
    result = "odd"

if is_prime(N):
    result += " prime"

print(result)