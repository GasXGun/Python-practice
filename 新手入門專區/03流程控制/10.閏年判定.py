while True:
    n = int(input())
    check = False
    if n%4==0:
        check = True
    if n%100==0:
        check = False
    if n%400==0:
        check = True
    print("Bissextile Year" if check else "Common Year")
