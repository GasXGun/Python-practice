first_day = int(input())
n = int(input())

total = 0
current = first_day

for day in range(1, n + 1):
    total += current
    current *= 2

print(f"第 {n} 天共存 {total} 元")