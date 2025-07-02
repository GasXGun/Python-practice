n = int(input())
foods = list(map(int, input().split()))
start, stop = map(int, input().split())

sum_satiety = sum(foods[start-1:stop])
print(sum_satiety)