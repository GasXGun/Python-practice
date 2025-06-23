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

k = int(input())
primes = []
i = 2
while len(primes) < k:
    if is_prime(i):
        primes.append(i)
    i += 1

print(','.join(map(str,primes)))
print(sum(primes))
#join會只在元素間加逗號
#map把primes每個數字轉成str
#要轉成str因為join()只能做字串序列
