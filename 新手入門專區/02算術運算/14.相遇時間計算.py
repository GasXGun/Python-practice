import math
m = int(input())
#all turn into meter(s)
d = m * 100
me = 100
fri = 30 * 2.54
dv = me - fri
ans = math.ceil(d/dv)
print(ans)
