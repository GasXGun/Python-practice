# point on line
a,b,c = map(int, input().split())
x,y = map(int, input().split())
if a*x + b*y + c == 0:
    print("YES")
else:
    print("NO")