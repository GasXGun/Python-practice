while True:
    n = int(input())
    num = []
    power = 0
    temp = n
    while temp>0:
        num.append(temp%10)
        temp //=10
        power += 1
    total = 0
    for i in num:
        total += i**power
    if total == n:
        print("YES")
    else:
        print("NO")
