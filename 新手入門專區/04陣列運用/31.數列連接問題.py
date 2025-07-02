import functools
n = int(input())
numbers = [input().strip() for _ in range(n)] 

# 自定義排序函數
def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

# 使用自定義排序
numbers.sort(key=functools.cmp_to_key(compare))

result = ''.join(numbers)
print(result)