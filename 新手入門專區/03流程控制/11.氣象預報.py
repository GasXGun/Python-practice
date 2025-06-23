#AQI
n = int(input())
for _ in range(n):
    t = int(input())
    check = False
    if t>37 and t <70:
        check = True
    elif t>150:
        check = True

    if check:
        print("避免外出")
    else:
        print("可依需要待在戶外")
