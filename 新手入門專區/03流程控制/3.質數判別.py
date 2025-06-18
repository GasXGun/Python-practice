#By 02-20.最大質數問題

#6n+-1
def  is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 ==0 or num%3 ==0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

#main
while True:
    n = int(input())
    if is_prime(n):
        print("YES")
    else:
        print("NO")
