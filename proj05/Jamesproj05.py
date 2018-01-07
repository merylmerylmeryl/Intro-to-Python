prefSuff = open ("rootsPrefixesSuffixes.txt", 'r')
rootList = []
prefList = []
suffList = []
list1 = []
list4 = []
for line in prefSuff:
    list2 = line.split()
    list1.append(list2[0:1])

indexRoots = list1.index(['#Roots'])
indexPref = list1.index(["#Prefixes"])
indexSuff = list1.index(["#Suffixes"])

rootList.append(list1[indexRoots+1:indexPref-1])
prefList.append(list1[indexPref+1:indexSuff-1])
suffList.append(list1[indexSuff+1:])


for objec in file('longWordList.txt'):
    objec = objec.split()
    objec = objec[0]
    list4.append(objec)

suffCountList = []
prefCountList = []
rootCountList = []

for word in list4:
    word = word.lower()
    count = 0
    for thing1 in rootList:
        for thing2 in thing1:
            for thing3 in thing2:
                if thing3 in word:
                    count+=1
            rootCountList.append(count)
    for thin1 in prefList:
        for thin2 in thin1:
            for thin3 in thin2:
                if word.startswith(thin3):
                    count +=1
                    prefCountList.append(count)
    for thi1 in suffList:
        for thi2 in thi1:
            for thi3 in thi2:
                if word.endswith(thi3):
                    count += 1
                    suffCountList.append(count)

print rootCountList

print "Roots"
print ""

for thing1 in rootList:
    for thing2 in thing1:
        for thing3 in thing2:
            for num in rootCountList:
                print "%-6s%10i"%(thing3,num)

print rootCountList
print""
print "Prefixes"
for thing1 in prefList:
    for thing2 in thing1:
        for thing3 in thing2:
            print thing3
            for num in prefCountList:
                print "%-6s%10i"%(thing3,num)
print""
print "Suffixes"
for thing1 in suffList:
    for thing2 in thing1:
        for thing3 in thing2:
            print thing3
            for num in suffCountList:
                print "%-6s%10i"%(thing3,num)
            
prefSuff.close()
