n = int(input())

for _ in range(n):
    num = int(input())
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i
    
    print(factorial)