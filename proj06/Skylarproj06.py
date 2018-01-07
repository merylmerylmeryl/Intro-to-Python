myFile = open("table.csv", "r")

#name: get_data_list
#param: FILE_NAME <str> - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists <list>
def get_data_list(FILE_NAME):
    data_list = []
    for thing in FILE_NAME:
        thing = thing.strip()
        thing = thing.split(",")
        data_list.append(thing)
    return data_list

#name: get_monthly_averages
#param: data_list <list> - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list <list>
def get_monthly_averages(data_list):
    data_list.remove(data_list[0])
    index1 = 0
    variableDate = data_list[index1][0][0:7]
    volumeList = []
    closeList = []
    averageList = []

    
    variableProduct = 0
    variableProductSum = 0
    volumeSum = 0
    variableQuotient = 0
        
    while data_list > 0:
        for line in data_list:
            line = data_list[index1][0][0:7]
            if line == variableDate:
                #[5] = volume
                #[6] = adj close
                volume = data_list[index1][5]
                volumeList.append(float(volume))
                close = data_list[index1][6]
                closeList.append(float(close))
    
                while volumeList > 0:
                    variable1 = volumeList[index1]
                    variable2 = closeList[index1]
                    variableProduct += float((variable2 * variable1))
                    variableProductSum += float(variableProduct)
                    volumeSum += float(volumeList[index1])
                    variableQuotient += float((variableProductSum / volumeSum))
                    averageList.append(variableQuotient)
                    volumeList.remove(volumeList[index1])
                    closeList.remove(closeList[index1])
                    index1 += 1
            else:
                variableDate = data_list[index1][0][0:7]
                    

        
    return monthly_average_list

#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info(monthly_average_list):
    return

# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the 
# return in monthly_average_list

# call print_info function with the monthly_average_list from above

z = get_data_list(myFile)
get_monthly_averages(z)
myFile.close()
