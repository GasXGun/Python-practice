money = int(input())
hundred, remainder = divmod(money,100)
ten, one = divmod(remainder, 10)
print(f"百元 {hundred}\n十元 {ten}\n壹元 {one}")
# 商數, 餘數 = divmod(被除數/除數)
# divmod(a,b)等價於(a//b, a%b)，不過實際上只做一次除法運算
