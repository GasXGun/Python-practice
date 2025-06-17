from decimal import Decimal,ROUND_HALF_UP
n = int(input())
sum = n*0.9
if n>800 and n<1500:
    sum = sum*0.9
elif n>=1500:
    sum = sum*0.79

print(Decimal(sum).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
