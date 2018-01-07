# proj07 10/20/08
# CSE 231 section 13

import string
import htmlFunctions


stopList = [line.strip().lower() for line in file('stop2.txt')]

def get_top_words(wordList = []):
    newList = wordList[:]
    updatedList = []
    wordDict = {}
    
    # Remove insignificant words from newList.
    for item in wordList:
        item = item.lower()
        if 'biden:' in item or 'palin:' in item or len(item) < 1:
            newList.remove(item)
        elif (item.startswith('(') and item.endswith(')')):
            newList.remove(item)

    # I originally just went through updatedList and did a .remove() for any
    # words that were in stopList, but every time you do a .remove(),
    # the index changes, so it kept getting screwed up and you wound up with
    # a list that still had some stopWords in it.

    # So instead, I created a new list (reusing the wordList variable by
    # resetting it to an empty list).  So now the program loops through
    # the updatedList.  If the word is NOT a stopword, it gets added to
    # the new list, wordList.
    wordList = []

    for item in newList:
        item = item.lower()
        item = item.strip(string.punctuation)
        if not item in stopList and len(item) > 0:
            wordList.append(item)

    for word in wordList:
        word = word.lower()
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

    sortedByNumber = []
    for word in wordDict:
        sortedByNumber.append((wordDict[word], word))
    sortedByNumber.sort()
    sortedByNumber = sortedByNumber[-1:-41:-1]

    sortedCopy = []
    for eachTuple in sortedByNumber:
        sortedCopy.append((eachTuple[1], eachTuple[0]))
    highest = sortedCopy[0][1]
    lowest = sortedCopy[-1][1]

    return [sortedCopy,highest,lowest]



def printHTMLfile(body,title):
    ''' create a standard html page with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    '''
    fd = open(title+'.html','w')
    theStr="""
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    <address></address>
    <!-- hhmts start --> Last modified: Fri Oct 10 10:09:41 EDT 2008 <!-- hhmts end -->
    </body> </html>
    """
    fd.write(theStr)
    fd.close()

def makeHTMLbox(body):
    ''' make and HTML box that has all the words in it
    '''
    boxStr = """<div style=\"
    width: 800px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\">%s</div>
    """
    return boxStr % (body)

def makeHTMLword(word,cnt,high,low):
    ''' make a word with a font size to be placed in the box. Font size is scaled
    between htmlBig and htmlLittle (to be user set). high and low represent the high 
    and low counts in the document. cnt is the cnt of the word 
    '''
    htmlBig = 96
    htmlLittle = 14
    ratio = (cnt-low)/float(high-low)
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    wordStr = '<span style=\"font-size:%spx;\">%s</span>'
    return wordStr % (str(fontsize), word)




bidenList = []
palinList = []

for line in file('debate2.txt'):
    # if the line starts with 'BIDEN:', then the list we're going to
    # want to add to is bidenList.
    if line.startswith('BIDEN:'):
        tempList = bidenList
    # if the line starts with 'PALIN:', then the list we're going to
    # want to add to is palinList.
    if line.startswith('PALIN:'):
        tempList = palinList
    if line.startswith('IFILL:'):
        tempList = []
    line = line.split()
    for word in line:
        word = word.strip().lower()
        tempList.append(word)

# Remove unnecessary words and punctuation from the lists using removal().
# Count the number of times each word appears using countEm.
bidenTops = get_top_words(bidenList)[0]
highCount = get_top_words(bidenList)[1]
lowCount = get_top_words(bidenList)[2]
body = ''

print "\nBiden Tops:\n", bidenTops
bidenTops = dict(bidenTops)

for word in bidenTops:
    cnt = bidenTops[word]
    body = body + makeHTMLword(word, cnt, highCount, lowCount) + ' '
box = makeHTMLbox(body)
printHTMLfile(box, 'biden')

palinTops = get_top_words(palinList)[0]
highCount = get_top_words(palinList)[1]
lowCount = get_top_words(palinList)[2]
body = ''

print "\nPalin Tops:\n", palinTops
palinTops = dict(palinTops)

for word in palinTops:
    cnt = palinTops[word]
    body = body + makeHTMLword(word, cnt, highCount, lowCount) + ' '
box = makeHTMLbox(body)
printHTMLfile(box, 'palin')
