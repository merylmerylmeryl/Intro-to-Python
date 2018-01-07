import string

def wordCount(file_name):

    tempList = []
    myList = []
    stopList = []
    myDict = {}
    
    for line1 in file(file_name):
        line1 = line1.strip()
        line1 = line1.split()
        for word1 in line1:
            word1 = word1.strip(string.punctuation)
            if word1 != '':
                tempList.append(word1)

    for line2 in file("stopWords.txt"):
        line2 = line2.strip()
        line2 = line2.split()
        for word2 in line2:
            word2 = word2.strip(string.punctuation)
            stopList.append(word2)

    for word3 in tempList:
        if word3.lower() not in stopList:
            myList.append(word3)

    for word4 in myList:
        if word4 not in myDict:
            myDict[word4] = 1
        else:
            myDict[word4] += 1

    print myDict

def compareFiles(file1,file2):
    
    tempList = []
    myList = []
    stopList = []
    
    for line1 in file(file1,file2):
        line1 = line1.strip()
        line1 = line1.split()
        for word1 in line1:
            word1 = word1.strip(string.punctuation)
            if word1 != '':
                tempList.append(word1)

    for line2 in file("stopWords.txt"):
        line2 = line2.strip()
        line2 = line2.split()
        for word2 in line2:
            word2 = word2.strip(string.punctuation)
            stopList.append(word2)

   



wordCount("gettysBurg.txt")
wordCount("declarationOfInd.txt")

compareFiles("gettysBurg.txt","declarationOfInd.txt")
