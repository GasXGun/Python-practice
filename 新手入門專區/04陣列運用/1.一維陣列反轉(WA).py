n = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]
print(' '.join(map(str, reversed_arr)))