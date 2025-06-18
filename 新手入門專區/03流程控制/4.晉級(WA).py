n = int(input())
subjects = []
pass_sub = []
for _ in range(n):
    sub, score = input().split()
    score = int(score)
    subjects.append((sub,score)) #用append()存入陣列列中
    if score >= 60:
        pass_sub.append(sub)

for sub in pass_sub:
    print(sub)

if len(pass_sub) >= n/2: #len->取陣列長度
    print("晉級")
else:
    print("失敗")
