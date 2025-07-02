digits = list(map(int, input().split(',')))
max_num = int(''.join(map(str, sorted(digits, reverse=True))))
min_num = int(''.join(map(str, sorted(digits))))
print(max_num - min_num)