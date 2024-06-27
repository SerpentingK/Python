words_list = ["Casa", "Juan", "Verde"]

def charsDic(lis):
    charsList = []
    wordsWithA = []
    dic = {}
    for i in lis:
        for j in i:
            if j.lower() not in charsList:
                charsList.append(j.lower())
            if j.lower() == "a" and i not in wordsWithA:
                wordsWithA.append(i)
    
    for i in charsList:
        dic[i] =  wordsWithA
    print(dic)  
    
charsDic(words_list)