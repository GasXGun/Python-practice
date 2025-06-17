s = int(input())
if s == 1:
    for i in range(1,6):
        if i == 1:
            print(' ' * 4 + '*')
        elif i == 5:
            print('*' * 9)
        else:
            print(' ' * (5-i) + '*' + ' ' * (2 * (i-1)-1) + '*')
elif s == 2:
    for i in range(1,6):
        print(' ' * (5-i) + '*' * (2*i -1))
elif s == 3:
    for i in range(5,0,-1):
        print(' ' * (5-i) + '*' * (2*i -1))
