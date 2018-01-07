# CSE 231, section 13
# proj 08, due Oct. 27, 2008


###############################################################################
# Tasks
# 1 - Create a training set
# 2 - Train a 'dumb' rule-based classifier
# 3 - Create a test set
# 4 - Apply rule-based classifier to test set
# 5 - Report accuracy of classifier
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and sums
# DONE - Do not modify.
###############################################################################
attributeList = []
attributeList.append("ID")
attributeList.append("radius")
attributeList.append("texture")
attributeList.append("perimeter")
attributeList.append("area")
attributeList.append("smoothness")
attributeList.append("compactness")
attributeList.append("concavity")
attributeList.append("concave")
attributeList.append("symmetry")
attributeList.append("fractal")
attributeList.append("class")



###############################################################################
# 1. Create a training set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
# makeTrainingSet
# parameters: 
#     - filename: name of the data file containing the training data records
#
# returns: trainingSet: a list of training records (each record is a dict,
#                       that contains attribute values for that record.)
###############################################################################
def makeTrainingSet(filename):
    # DONE - Do not modify.
    trainingSet = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        # Create a dictionary for the line
        # ( assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys )
        record = {}
        for i in range(len(attributeList)):
              if(i==11): #class label is a character, not a float
                  record[attributeList[i]] = linelist[31].strip() 
              else:
                  record[attributeList[i]] = float(linelist[i])
        # Add the dictionary to a list
        trainingSet.append(record)        

    return trainingSet

###############################################################################
# 2. Train 'Dumb' Classifier
# trainClassifier
# parameters:
#     - trainingSet: a list of training records (each record is a dict,
#                     that contains attribute values for that record.)
#
# returns: a dictionary of midpoints between the averages of each attribute's
#           values for benign and malignant tumors
###############################################################################
def helper1(dictionary):
    dictionary["radius"] = 0
    dictionary["texture"] = 0
    dictionary["perimeter"] = 0
    dictionary["area"] = 0
    dictionary["smoothness"] = 0
    dictionary["compactness"] = 0
    dictionary["concavity"] = 0
    dictionary["concave"] = 0
    dictionary["symmetry"] = 0
    dictionary["fractal"] = 0
    return dictionary

def helper2(sums, counts):
    for key in sums:
        sums[key] = sums[key] / counts[key]
    return sums


def trainClassifier(trainingSet):

    # TODO
    
    # A. initialize dictionaries for sums of attribute values
    #    and initialize record counts
    malignant = helper1({})
    malignantCounts = helper1({})
    benign = helper1({})
    benignCounts = helper1({})


    # B. process each record in the training set
    #    calculating sums and counts as we go
    for record in trainingSet:
        if record["class"] == "M":
            for i in record:
                if i != "class" and i != "ID":
                    malignant[i] += record[i]
                    malignantCounts[i] += 1
        elif record["class"] == "B":
            for i in record:
                if i != "class" and i != "ID":
                    benign[i] += record[i]
                    benignCounts[i] += 1

    # C. calculate averages
    malignant = helper2(malignant, malignantCounts)
    benign = helper2(benign, benignCounts)


    # D. calcualte midpoints for our classifier
    classifier = {}
    for key in malignant:
        classifier[key] = (malignant[key] + benign[key]) / 2
    print classifier

    return [classifier, malignant, benign]



###############################################################################
# 3. Create a test set
# - Read in file
# - Create a dictionary for each line
# - Initialize each record's predicted class to '0'
# - Add this dictionary to a list
#
# makeTestSet
# parameters: 
#     - filename: name of the data file containing the test data records
#
# returns: testSet: a list of test records (each record is a dict,
#                       that contains attribute values for that record
#                       and where the predicted class is set to 0. 
###############################################################################
def makeTestSet(filename):

    # DONE - Do not modify.
    testset = makeTrainingSet(filename)

    for record in testset:
        record["predicted"] = 0

    return testset


###############################################################################
# 4. Classify test set
#
# classifyTestRecords
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#      - classifier: a dictionary of midpoint values for each attribute
#
# returns: testSet with the predicted class set to either 2 (benign) or 4 (malignant)
#
# for each record, if the majority of attributes are greater than midpoint
# then predict the record as malignant
###############################################################################
def classifyTestRecords(testSet, classifier):
    
    # For each record in testset
    for record in testSet:
        # initialize malignant and benign votes to zero
        malignantVotes = 0
        benignVotes = 0
        # for each attribute of the record
        for i in record:
            # if attribute value is greater than midpoint then
            # add one to malignant vote. Otherwise, add one to benign vote
            if i != "ID" and i != "class" and i != "predicted":
                if record[i] > classifier[i]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
        # if malignant vote greater than or equal to benign vote then
        # predicted class of record is malignant (set predicted class value)
        # otherwise, the predicted class is benign
        if malignantVotes >= benignVotes:
            classType = "M"
        else:
            classType = "B"

        record["predicted"] = classType
    return testSet


###############################################################################
# 5. Report Accuracy
# reportAccuracy
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#                 and both the predicted and actual class values are set
#
# returns: None
#
# prints out the number correct / total and accuracy as a percentage
###############################################################################
def reportAccuracy(testSet):

    accuracyCounts = 0
    allCounts = 0
    
    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class ("predicted") to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.
    for record in testSet:
        if record["class"] == record["predicted"]:
            accuracyCounts += 1
        allCounts += 1

    print "The classifier correctly predicted the class (malignant/benign) \
of", accuracyCounts, "records out of", allCounts, "records."
    print "The classifier achieved an accuracy of", str(round(((float(accuracyCounts) / allCounts) * 100), 2)), "percent."


###############################################################################
def dumpStats(classifier,benignAverages,malignantAverages):

# print out the averages and classifier cutoff for each of the 9 categories
# format string to reproduce the table in the demo is
# print '%28s %12.3f %12.3f %12.3f'%(key,malignanAvg[key],classifier[key],benignAvg[key])
    print "Classifier, benign, and malignant stats"
    print "=" * 73
    print "%28s %12s %12s %12s"%("Key", "Malignant", "Classifier", "Benign")
    print "%28s %12s %12s %12s"%("", "Average", "Midpoint", "Average")
    for key in classifier:
        print "%28s %12.3f %12.3f %12.3f"%(key, benignAverages[key], classifier[key], malignantAverages[key])

def checkSomePatients(testDataRecordsList, classifier):
    check = ""
# starts a prompting loop. Prompts for a patient ID
# for each value, prints out the patient's value, the classifier cutoff and the diagnosis
# prints out the final diagnosis
    print "%28s %12s %12s %12s"%("Key", "Patient", "Classifier", "Class")
    print "%28s %12s %12s %12s"%("", "Value", "Cutoff", "")
    while True:
        check = raw_input("Type an ID to check a patient (\"quit\" to stop): ")
        if check == "quit":
            break
        for record in testDataRecordsList:
            if record["ID"] == float(check):
                patient = record
        if not float(check) in record:
            continue
        print "Checking patient ID:", check
        for key in patient:
            if key != "ID" and key != "class" and key != "predicted":
                if patient[key] > classifier[key]:
                    theClass = "Malignant"
                else:
                    theClass = "Benign"
                print "%28s %12.3f %12.3f %12s"%(key, patient[key], classifier[key], theClass)
        print "Overall Diagnosis for patient", patient["ID"],":", patient["predicted"] 
    
###############################################################################
# main - starts the program
###############################################################################
def main():
    # TODO
    
    print "Reading in training data..."
    trainingSet = []
    trainingFile = "cancerTrainingData.txt"
    trainingSet = makeTrainingSet(trainingFile)
    print "Done reading training data.\n"

    print "Training classifier..."    
    classifier = trainClassifier(trainingSet)[0]
    print "Done training classifier.\n"

    print "Present Classifier Stats"
    dumpStats(classifier, trainClassifier(trainingSet)[1], trainClassifier(trainingSet)[2])

    print "Reading in test data..."
    testFile = "cancerTestingData.txt"
    testSet = makeTestSet(testFile)
    print "Done reading test data.\n"

    print "Classifying records..."
    testSet = classifyTestRecords(testSet, classifier)

    print "Done classifying.\n"
    reportAccuracy(testSet)

    print "\nCheck some Patients"
    checkSomePatients(testSet, classifier)    

    print "Program finished."
    
main()
