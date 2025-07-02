# 比大小
n1,n2,n3 = map(int, input().split())
display = input()
if display == 'Asc':
    res = sorted([n1, n2, n3])
    print(*res,sep='<')
elif display == 'Desc':
    res = sorted([n1, n2, n3], reverse=True)
    print(*res, sep='>')