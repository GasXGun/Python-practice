from decimal import Decimal, getcontext, ROUND_HALF_UP

x1, y1 = map(Decimal, input().split())
x2, y2 = map(Decimal, input().split())

dist = ((x1 - x2)**2 + (y1 - y2)**2).sqrt()
print(dist.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
