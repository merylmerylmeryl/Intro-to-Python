# CSE 231, section 13
# proj05

tempList = []

rootsList = []
prefixList = []
suffixList = []

wordList = []

# go through the rootsPrefixesSuffixes file and add all the roots, prefixes, and suffixes to a list
for line in file('rootsPrefixesSuffixes.txt'):
    if not line.startswith('#'):
        part = line.split()
        if len(part) > 0:
            part = part[0].lower()
            tempList.append(part)

#go through the list of roots, prefixes, and suffixes and separate them into
# their respective lists
for x in range(0, 11):
    rootsList.append(tempList[x])
for y in range(11,22):
    prefixList.append(tempList[y])
for z in range(22,30):
    suffixList.append(tempList[z])

print "Reading Roots..."
print "Reading Prefixes..."
print "Reading Suffixes..."
print "Counting..."
print "Printing results..."

# add all the words from longWordList.txt to a list
for line in file('longWordList.txt'):
    line = line.split()
    line = line[0].lower()
    wordList.append(line)

print "\nRoots:\n"


# compare each root with all the words in wordList.  1 is added to the counter
# each time a root is found in a word.  Print the root along with the number of
# times it appears in wordList.
for root in rootsList:
    counter = 0
    for word in wordList:
        if root in word:
            counter+=1
    print "%-6s%10i"%(root.strip(), counter)

print "\nPrefixes:\n"

# compare each prefix with all the words in wordList.  1 is added to the counter
# each time a prefix begins a word.  Print the prefix along with the number of
# times it appears in wordList.
for prefix in prefixList:
    counter = 0
    for word in wordList:
        if word.startswith(prefix):
            counter +=1
    print "%-6s%10i"%(prefix.strip(), counter)

print "\nSuffixes:\n"

# compare each prefix with all the words in wordList.  1 is added to the counter
# each time a suffix ends a word.  Print the suffix along with the number of
# times it appears in wordList.
for suffix in suffixList:
    counter = 0
    for word in wordList:
        if word.endswith(suffix):
            counter+=1
    print "%-6s%10i"%(suffix.strip(), counter)
