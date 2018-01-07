# CSE 231 section 13
# proj07 due 10/20/08

import string
import htmlFunctions
from Stemmer2 import *


stopList = [line.strip().lower() for line in file('stop2.txt')]

def removal(wordList = []):
    newList = wordList[:]
    updatedList = []
    
    # Remove insignificant words from newList. Use wordList to determine
    # what words are insignificant.
    for item in wordList:
        if 'BIDEN:' in item or 'PALIN:' in item or len(item) < 1:
            newList.remove(item)
        if item.startswith('(') and item.endswith(')'):
            newList.remove(item)

    # Remove punctuation from remaining words in wordList.
    for item in newList:
        newString = ''
        for char in item:
            if char not in string.punctuation:
                newString += char
        if len(newString) > 0:
            updatedList.append(newString)

    # I originally just went through updatedList and did a .remove() for any
    # words that were in stopList, but every time you do a .remove(),
    # the index changes, so it kept getting screwed up and you wound up with
    # a list that still had some stopWords in it.

    # So instead, I created a new list (reusing the wordList variable by
    # resetting it to an empty list).  So now the program loops through
    # the updatedList.  If the word is NOT a stopword, it gets added to
    # the new list, wordList.
    wordList = []

    for item in updatedList:
        if not item.lower() in stopList:
            wordList.append(item)

    return wordList


def countEm(wordList = []):
    myStemmer = Stemmer('english')
    countList = []
    longList = []


    # Go through wordList.  Compare each word to every single other word
    # in the list.  If the stems are the same, make the variable 'longest'
    # equal to the longer of the two words.  Keep appending to the longList.
    # We'll end up with a list of words whose stems will not be repeated
    # in the list.
    for word in set(wordList):
        longest = word
        for thing in wordList:
            if myStemmer.stemWord(word) == myStemmer.stemWord(thing):
                if len(thing) > len(word):
                    longest = thing
        if longest not in longList:
            longList.append(longest)

    longList = set(longList)
    print longList

##    for word in longList:
##        count = 0
##        for item in wordList:
##            if myStemmer.stemWord(word.lower()) == myStemmer.stemWord(item.lower()):
##                count += 1
##        countList.append(count)
##
##    
##    return countList



# Zip the words in the word lists with their corresponding counts in the count
# lists.
def get_top_words(words = [], num = []):
    wordZip = zip(words, num)
    wordDict = dict(wordZip)

    sortedByNumber = sorted(wordDict.items(), key=lambda(k,v):(v,k))
    highest = sortedByNumber[-1][1]
    lowest = sortedByNumber[0][1]
    dictSorted = dict(sortedByNumber[-1:-41:-1])
     
    return [dictSorted,highest,lowest]



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

for line in file('debate.txt'):
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
        word = word.strip()
        tempList.append(word)

# Remove unnecessary words and punctuation from the lists using removal().
# Count the number of times each word appears using countEm.
bidenList = removal(bidenList)
bidenCount = countEm(bidenList)
bidenCount
##bidenTops = get_top_words(bidenList, bidenCount)[0]
##highCount = get_top_words(bidenList, bidenCount)[1]
##lowCount = get_top_words(bidenList, bidenCount)[2]
##body = ''
##
##for word in bidenTops:
##    cnt = bidenTops[word]
##    body = body + makeHTMLword(word, cnt, highCount, lowCount) + ' '
##box = makeHTMLbox(body)
##printHTMLfile(box, 'biden')
##
##
##
##
##palinList = removal(palinList)
##palinCount = countEm(palinList)
##palinTops = get_top_words(palinList, palinCount)[0]
##highCount = get_top_words(palinList, palinCount)[1]
##lowCount = get_top_words(palinList, palinCount)[2]
##body = ''
##
##
##for word in palinTops:
##    cnt = palinTops[word]
##    body = body + makeHTMLword(word, cnt, highCount, lowCount) + ' '
##box = makeHTMLbox(body)
##printHTMLfile(box, 'palin')
##
##print "Biden\n", bidenTops, '\n'
##print "Palin\n", palinTops

