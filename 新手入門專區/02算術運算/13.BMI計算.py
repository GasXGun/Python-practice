from decimal import Decimal, ROUND_HALF_UP
w, h = map(int, input().split())
bmi = Decimal(w) / (Decimal(h) / Decimal(100)) ** 2 #所有運算元都要轉乘Decimal型
print(bmi.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
