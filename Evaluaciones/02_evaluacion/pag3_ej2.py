words = []

def wordsToDict(words):
    charsDict = dict()
    charsList = list()
    for i in words:
        for j in i:
            if j.lower() not in charsList:
                charsDict[j.lower()] = ""
        for j in charsDict:
            wordsList = []
            for k in words:
                if k.lower().count(j) > 1:
                    wordsList.append(k)
            charsDict[j] = wordsList
    print(charsDict)

c = int(input("Ingrese numero de palabras: "))
for i in range(c):  
    newWord = input(f"Ingrese palabra {i + 1}:")
    words.append(newWord)
wordsToDict(words)