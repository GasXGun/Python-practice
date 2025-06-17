n = int(input())
if n<0:
    print(bin(n & 0b11111111)[2:])# & 0b11111111取8位二補數以表
else:
    print(bin(n)[2:].zfill(8))
# bin用於轉2進位
# [2:]用於去掉'0b'前綴
# zfill 補位用
