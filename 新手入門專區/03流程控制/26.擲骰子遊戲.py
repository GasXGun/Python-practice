A, B, C = map(int, input().split())
total = A + B + C
result = 'H' if total > 9 else 'L'
print(f"{total} {result}")