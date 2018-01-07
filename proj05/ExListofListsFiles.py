
# list of possible digits that could be in our file
listOfNums=[1,2,3,4,5,6,7,8,9]

# initialize list of lists, each list contains a possible
# digit and the number of times it is found (0 to start)
countList=[]
for num in listOfNums:
    countList.append([num,0])

# read each line of our file, strip the whitespace at begin and end
# split the line into list of digits
for line in file("numbers.txt"):
    line=line.strip()
    lineAsList=line.split()

    # for each digit on this line of file (now in list), find where this
    # digit appears in listOfNums, then know it will be found at same index
    # in countList.  Increment count for this digit in countList
    for num in lineAsList:
        num=int(num)
        ind = listOfNums.index(num)
        countList[ind][1] += 1

# output the numbers and counts in nice columns
print "%5s %5s"%("num","count")
for entry in countList:
    print "%5d %5d"%(entry[0],entry[1])

            
    
    
