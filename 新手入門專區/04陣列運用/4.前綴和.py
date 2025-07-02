n = int(input())
A = list(map(int, input().split()))
B = []
current_sum = 0
for num in A:
    current_sum += num
    B.append(str(current_sum))
print(' '.join(B))