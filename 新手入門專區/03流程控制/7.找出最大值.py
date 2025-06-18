n = int(input())
big = 0
for i in range(n):
    x = int(input())
    if(i==0):
        # print(f"{x} first")
        big = x
    else:
        big = max(big,x)
print(big)
