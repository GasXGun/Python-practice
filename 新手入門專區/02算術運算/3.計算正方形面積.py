from decimal import Decimal, ROUND_HALF_UP

n = int(input())
for i in range(n):
    w = float(input()) #可能是浮點數
    print(Decimal(w*w).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
# 四捨五入用round會搞 所以要用decimal模組中的quantisize進行四捨五入
# rounding可以設定強制四捨五入ROUND_HALF_UP
