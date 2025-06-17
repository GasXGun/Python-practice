sh,sm = map(int,input().split())
eh,em = map(int,input().split())

#計算時間差
if eh<sh: #隔天
    eh += 24

if em<sm: #分鐘不夠補
    minute = (eh-1-sh)*60 + em+60-sm
else:
    minute = (eh-sh)*60 +em-sm

#計算價錢
if minute <= 120:
    price = minute//30 *30
elif minute <240:
    price = 120 + (minute-120)//30 *40
else:
    price = 280 + (minute-240)//30 *60

print(price)
#要用//，python不會自動算成整數
