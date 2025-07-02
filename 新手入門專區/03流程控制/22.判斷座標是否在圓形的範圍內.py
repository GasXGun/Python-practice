# point in the circle
import math
x,y = map(int, input().split())
r = 100
if x**2 + y**2 <= r**2:
    print("inside")
else:
    print("outside")