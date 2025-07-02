n = int(input())
scores = []
cnt1 = 0
cnt2 = 0
for _ in range(n):
    s = int(input())
    if s>= 900:
        cnt1 += 1
    if s >= 600 and s<= 700:
        cnt2 += 1
    scores.append(s)
print(max(scores))
print(cnt1)
print(cnt2)
avg = sum(scores) / n
print(round(avg, 1)) #四捨五入到小數點第一位
