m, n = map(int, input().split())
#f""中，{}內會輸出該值
print(f"{m}+{n}={m+n}")
print(f"{m}*{n}={m*n}")
print(f"{m}-{n}={m-n}")

ans1 = m // n #//:直接取整
ans2 = m % n

if ans2 < 0:
    ans2 += abs(n) # 餘數為正
    ans1 = (m - ans2) // n

if ans2 == 0:
    print(f"{m}/{n}={ans1}")
else:
    print(f"{m}/{n}={ans1}...{ans2}")
#該題在test上有問題
