from decimal import Decimal,ROUND_HALF_UP
s,t = map(int,input().split())
# s:時數
# t:時薪
if s<=60:
    sum = s*t
elif s<=120:
    sum = 60*t + (s-60)*t*1.33
else:
    sum = 60*t + 60*t*1.33 + (s-120)*t*1.66
print(Decimal(sum).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
