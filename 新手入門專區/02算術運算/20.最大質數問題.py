#6n+-1
def  is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 ==0 or num%3 ==0:
        return True
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

def solve(n):
    j = n-1
    while j>=2:
        if j==2 or j==3:
            return j
        if (j%6==1 or j%6==5):
            if is_prime(j):
                return j
        j -= 1
    

n = int(input())
ans = solve(n)
print(ans)
