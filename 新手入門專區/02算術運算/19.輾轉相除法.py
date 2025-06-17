m,n = map(int,input().split())
while n != 0:
    m,n = n, m%n
print(m)
