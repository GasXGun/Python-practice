dic = {"dog":"狗", "cat":"貓", "duck":"鴨", "cow":"牛", "fox":"狐"}
# dictionary
while True:
    word = input()
    if word in dic:
        print(dic[word])
    else:
        for key,value in dic.items():
            if value == word:
                print(key)
                break
            
