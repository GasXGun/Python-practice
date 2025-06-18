while True:
    p = int(input())
    if p>=100:
        p*=0.7
    elif p>=30:
        p*=0.8
    elif p>=10:
        p*=0.9

    print(int(p*100))
