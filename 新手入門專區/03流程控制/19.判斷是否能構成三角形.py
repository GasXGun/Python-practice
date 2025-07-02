# triangle
n1,n2,n3 = map(int, input().split())
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("fit")
else:
    print("unfit")