n = int(input())
p = input().strip()
T = int(input())

groups = [p[i:i+T] for i in range(0, n, T)]
print(' '.join(groups))