vowels = {'a','e','i','o','u'}
while True:
    s = input().lower() #.lower()全部轉小寫
    if s in vowels:
        print("母音")
    else:
        print("子音")
