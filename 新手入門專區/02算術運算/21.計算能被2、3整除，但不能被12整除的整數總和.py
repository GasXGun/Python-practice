n = int(input())
sum = 0
for i in range(1,n,1):
    if i%2==0 and i%3==0 and i%12!=0:
        sum += i
print(sum)
