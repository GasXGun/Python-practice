n = int(input())
A = list(map(int, input().split()))
if n == 0:
    print()
elif n == 1:
    print(A[0])
else:
    B = [A[0]]
    for i in range(1, n):
        B.append(A[i] - A[i-1])
    print(' '.join(map(str, B)))