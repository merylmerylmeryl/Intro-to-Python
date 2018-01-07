


import commands


print
print
print "Welcome to the grader."
print
print




#commands.getoutput('python solution.py > studentSolution.txt')
commands.getoutput('python proj05.py > studentSolution.txt')   #use this line for grading students

studentSolutionFile = open("studentSolution.txt")

studentSolution = studentSolutionFile.readlines()


studentSolutionList = []

for line in studentSolution:
    studentSolutionList.append(line.strip())
    

count = 0
foundAnError = False

print "These lines are correct!"
print "************************"

wordFile = raw_input("which solution file are we grading against (e.g. mediumWordListSolution.txt)? ")

try:

    for line in file(wordFile):
        if count > len(studentSolutionList)-1:
            print "there are no more lines in the student solution, but there should be at least this next line"
            print line.strip()
            foundAnError = True        
            break
            
        #print "solution line:", line, "!"
        #print "student  line:", studentSolutionList[0], "!"
        if line.strip() == studentSolutionList[count]:
            print line.strip()
        else:
            print "************************"
            print
            print
            print "Too bad. You're not there yet."
            print
            print "The next line is what it was supposed to be, and the line after that is what your code produced: "
            print line.strip()
            print studentSolutionList[count]
            foundAnError = True
            break
            
        count += 1


    if (foundAnError):
        print 
        print "Keep at it. You'll get there!"
    else:
        print "************************"
        print
        print "CONGRATULATIONS!!! Your code is producing the right output. Now make sure your coding style is up to snuff!"
            

except IOError:
    print "Error: The file ", wordFile, " does not exist. Please make sure you have placed it in the same directory as gradeIt.py"

