from decimal import Decimal,ROUND_HALF_UP
f = float(input())
print(Decimal(f*(9/5)+32).quantize(Decimal('0.1'),rounding = ROUND_HALF_UP))
#又Decimal
