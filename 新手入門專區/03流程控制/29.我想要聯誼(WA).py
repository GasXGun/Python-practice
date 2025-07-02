N = int(input())
girls = input().split()
K = input()

count = 0

for traits in girls:
    if K in traits:
        count += 1

print(count)