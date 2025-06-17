n = int(input())
#Q:0 hours or 0 hour?

#分別計算
d = n//(60*60*24)
n -= d*60*60*24
h = n//(60*60)
n -= h*60*60
m = n//60
s = n%60

#輸出，注意1的問題 90061
if d == 1:
    print("1 day")
else:
    print(f"{d} days")
    
if h == 1:
    print("1 hour")
else:
    print(f"{h} hours")
    
if m == 1:
    print("1 minute")
else:
    print(f"{m} minutes")

if s == 1:
    print("1 second")
else:
    print(f"{s} seconds")
