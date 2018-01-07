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
attributeList.append("radius_se")
attributeList.append("texture_se")
attributeList.append("perimeter_se")
attributeList.append("area_se")
attributeList.append("smoothness_se")
attributeList.append("compactness_se")
attributeList.append("concavity_se")
attributeList.append("concave_se")
attributeList.append("symmetry_se")
attributeList.append("fractal_se")
attributeList.append("radius_worst")
attributeList.append("texture_worst")
attributeList.append("perimeter_worst")
attributeList.append("area_worst")
attributeList.append("smoothness_worst")
attributeList.append("compactness_worst")
attributeList.append("concavity_worst")
attributeList.append("concave_worst")
attributeList.append("symmetry_worst")
attributeList.append("fractal_worst")
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
              if(i==31): #class label is a character, not a float
                  record[attributeList[i]] = linelist[i].strip() 
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
def trainClassifier(trainingSet):
    
    # A. initialize dictionaries for sums of attribute values
    #    and initialize record counts
    radiusSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    textureSum = {"M":0, "B":0, "Mav": 0, "Bav":0}
    perimeterSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    areaSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    smoothnessSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    compactnessSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    concavitySum = {"M":0, "B":0, "Mav":0, "Bav":0}
    concaveSum = {"M":0, "B":0, "Mav":0, "Bav":0}
    symmetrySum = {"M":0, "B":0, "Mav":0, "Bav":0}
    fractalSum = {"M":0, "B":0, "Mav":0, "Bav":0}

    MradiusCount = 0
    MtextureCount = 0
    MperimeterCount = 0
    MareaCount = 0
    MsmoothnessCount = 0
    McompactnessCount = 0
    MconcavityCount = 0
    MconcaveCount = 0
    MsymmetryCount = 0
    MfractalCount = 0

    BradiusCount = 0
    BtextureCount = 0
    BperimeterCount = 0
    BareaCount = 0
    BsmoothnessCount = 0
    BcompactnessCount = 0
    BconcavityCount = 0
    BconcaveCount = 0
    BsymmetryCount = 0
    BfractalCount = 0

    # B. process each record in the training set
    #    calculating sums and counts as we go
    for record in trainingSet:
        if record["class"] == "M":
            for i in record:
                if i == "radius":
                    radiusSum["M"] += record[i]
                    MradiusCount += 1
                elif i == "texture":
                    textureSum["M"] += record[i]
                    MtextureCount += 1
                elif i == "perimeter":
                    perimeterSum["M"] += record[i]
                    MperimeterCount += 1
                elif i == "area":
                    areaSum["M"] += record[i]
                    MareaCount += 1
                elif i == "smoothness":
                    smoothnessSum["M"] += record[i]
                    MsmoothnessCount += 1
                elif i == "compactness":
                    compactnessSum["M"] += record[i]
                    McompactnessCount += 1
                elif i == "concavity":
                    concavitySum["M"] += record[i]
                    MconcavityCount += 1
                elif i == "concave":
                    concaveSum["M"] += record[i]
                    MconcaveCount += 1
                elif i == "symmetry":
                    symmetrySum["M"] += record[i]
                    MsymmetryCount += 1
                elif i == "fractal":
                    fractalSum["M"] += record[i]
                    MfractalCount += 1
        elif record["class"] == "B":
            for i in record:
                if i == "radius":
                    radiusSum["B"] += record[i]
                    BradiusCount += 1
                elif i == "texture":
                    textureSum["B"] += record[i]
                    BtextureCount += 1
                elif i == "perimeter":
                    perimeterSum["B"] += record[i]
                    BperimeterCount += 1
                elif i == "area":
                    areaSum["B"] += record[i]
                    BareaCount += 1
                elif i == "smoothness":
                    smoothnessSum["B"] += record[i]
                    BsmoothnessCount += 1
                elif i == "compactness":
                    compactnessSum["B"] += record[i]
                    BcompactnessCount += 1
                elif i == "concavity":
                    concavitySum["B"] += record[i]
                    BconcavityCount += 1
                elif i == "concave":
                    concaveSum["B"] += record[i]
                    BconcaveCount += 1
                elif i == "symmetry":
                    symmetrySum["B"] += record[i]
                    BsymmetryCount += 1
                elif i == "fractal":
                    fractalSum["B"] += record[i]
                    BfractalCount += 1

    
    # C. calculate averages
    radiusSum["Mav"] = radiusSum["M"] / MradiusCount
    textureSum["Mav"] = textureSum["M"] / MtextureCount
    perimeterSum["Mav"] = perimeterSum["M"] / MperimeterCount
    areaSum["Mav"] = areaSum["M"] / MareaCount
    smoothnessSum["Mav"] = smoothnessSum["M"] / MsmoothnessCount
    compactnessSum["Mav"] = compactnessSum["M"] / McompactnessCount
    concavitySum["Mav"] = concavitySum["M"] / MconcavityCount
    concaveSum["Mav"] = concaveSum["M"] / MconcaveCount
    symmetrySum["Mav"] = symmetrySum["M"] / MsymmetryCount
    fractalSum["Mav"] = fractalSum["M"] / MfractalCount

    radiusSum["Bav"] = radiusSum["B"] / BradiusCount
    textureSum["Bav"] = textureSum["B"] / BtextureCount
    perimeterSum["Bav"] = perimeterSum["B"] / BperimeterCount
    areaSum["Bav"] = areaSum["B"] / BareaCount
    smoothnessSum["Bav"] = smoothnessSum["B"] / BsmoothnessCount
    compactnessSum["Bav"] = compactnessSum["B"] / BcompactnessCount
    concavitySum["Bav"] = concavitySum["B"] / BconcavityCount
    concaveSum["Bav"] = concaveSum["B"] / BconcaveCount
    symmetrySum["Bav"] = symmetrySum["B"] / BsymmetryCount
    fractalSum["Bav"] = fractalSum["B"] / BfractalCount

    # D. calcualte midpoints for our classifier
    radiusMidpoint = (radiusSum["Mav"] + radiusSum["Bav"])/2
    textureMidpoint = (textureSum["Mav"] + textureSum["Bav"])/2
    perimeterMidpoint = (perimeterSum["Mav"] + perimeterSum["Bav"])/2
    areaMidpoint = (areaSum["Mav"] + areaSum["Bav"])/2
    smoothnessMidpoint = (smoothnessSum["Mav"] + smoothnessSum["Bav"])/2
    compactnessMidpoint = (compactnessSum["Mav"] + compactnessSum["Bav"])/2
    concavityMidpoint = (concavitySum["Mav"] + concavitySum["Bav"])/2
    concaveMidpoint = (concaveSum["Mav"] + concaveSum["Bav"])/2
    symmetryMidpoint = (symmetrySum["Mav"] + symmetrySum["Bav"])/2
    fractalMidpoint = (fractalSum["Mav"] + fractalSum["Bav"])/2

    # return classifier
    classifier = {"radius":radiusMidpoint, "texture":textureMidpoint,\
                  "perimeter":perimeterMidpoint, "area":areaMidpoint,\
                  "smoothness":smoothnessMidpoint, "compactness":compactnessMidpoint,\
                  "concavity":concavityMidpoint, "concave":concaveMidpoint,\
                  "symmetry":symmetryMidpoint, "fractal":fractalMidpoint}

    return classifier


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

    # TODO
    
    # for each record in testset
    for record in testSet:
        # initialize malignant and benign votes to zero
        malignantVotes = 0
        benignVotes = 0

        # for each attribute of the record
            # if attribute value is greater than midpoint then
            # add one to malignant vote. Otherwise, add one to benign vote
        for i in record:
            if i == "radius":
                if record[i] > classifier["radius"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "texture":
                if record[i] > classifier["texture"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "perimeter":
                if record[i] > classifier["perimeter"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "area":
                if record[i] > classifier["area"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "smoothness":
                if record[i] > classifier["smoothness"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "compactness":
                if record[i] > classifier["compactness"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "concavity":
                if record[i] > classifier["concavity"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "concave":
                if record[i] > classifier["concave"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "symmetry":
                if record[i] > classifier["symmetry"]:
                    malignantVotes += 1
                else:
                    benignVotes += 1
            elif i == "fractal":
                if record[i] > classifier["fractal"]:
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

        record["class"] = classType

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
    pass
    # TODO

    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class ("predicted") to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.

###############################################################################
def dumpStats(classifier,benignAverages,malignantAverages):
    pass
# TODO
# print out the averages and classifier cutoff for each of the 9 categories
# format string to reproduce the table in the demo is
# print '%28s %12.3f %12.3f %12.3f'%(key,malignanAvg[key],classifier[key],benignAvg[key])


def checkSomePatients(testDataRecordsList, classifier):
    pass
# TODO
# starts a prompting loop. Prompts for a patient ID
# for each value, prints out the patient's value, the classifier cutoff and the diagnosis
# prints out the final diagnosis

    
###############################################################################
# main - starts the program
###############################################################################
def main():
    
    print "Reading in training data..."
    trainingSet = []
    trainingFile = "cancerTrainingData.txt"
    print "Done reading training data.\n"

    print "Training classifier..."    
    trainingSet = makeTrainingSet(trainingFile)
    classifier = trainClassifier(trainingSet)
    print "Done training classifier.\n"

    print "Classifier, benign and malignant stats"
    

    print "Reading in test data..."
    testFile = "cancerTestingData.txt"
    testSet = makeTestSet(testFile)
    print "Done reading test data.\n"

    print "Classifying records..."
    classifyTestRecords(testSet, classifier)
    print "Done classifying.\n"
    # add call to appropriate function

    print "Check some Patients"
    # add call to appropriate function    

    print "Program finished."
    
main()
