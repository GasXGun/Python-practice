n = int(input())
s1 = int(n/10);
n -= 10*s1
s2 = int(n/5)
s3 = n-5*s2
print(f"NT10={s1}\nNT5={s2}\nNT1={s3}")
