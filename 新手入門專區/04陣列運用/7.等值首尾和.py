n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)
suffix = [0] * (n + 1)

# 計算前綴和
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# 計算後綴和
for i in range(n - 1, -1, -1):
    suffix[i] = suffix[i + 1] + arr[i]

count = 0
i = 1
j = n - 1

while i <= n and j >= 0:
    if prefix[i] == suffix[j]:
        count += 1
        i += 1
        j -= 1
    elif prefix[i] < suffix[j]:
        i += 1
    else:
        j -= 1

print(count)