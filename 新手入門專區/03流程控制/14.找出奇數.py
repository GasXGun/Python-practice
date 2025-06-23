n = int(input())
for i in range(1,n+1,2):
    if i+2 >= n+1:
        print(i,end='\n')
    else:
        print(i,end=' ')#使輸出空格而非換行
