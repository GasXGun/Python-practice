t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    ans = 0
    for i in range(min(m,n),max(m,n)+1):
        ans += i
    print(ans)
