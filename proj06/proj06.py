# CSE 231, section 13
# proj06

stocksFile = open('table.csv', 'r')

# make a list of the stock's records' lists
def get_data_list(FILE_NAME):
    data_list = []
    for line in FILE_NAME:
        line = line.strip().split(",")
        if not line[0][0].isalpha():
            data_list.append(line)
    return data_list

# make a list of the stock's monthly averages and their corresponding dates
def get_monthly_averages(data_list):
    monthly_average_list = []
    dataSum = 0
    volumeDenom = 0
    # find the first month/year in the data file and create a variable for it
    monthyear = data_list[0][0][0:7]
    # go through each group of data (representing a split-up version of each
    # line in the data file) and set variables equal to the Date, Volume, and
    # Adj Close
    for group in data_list:
        date = group[0]
        volume = float(group[-2])
        close = float(group[-1])
        newGroup = [date, volume * close]
        # if we're on the last day, calculate the average and append that along
        # with the month and year to monthly_average_list.
        if data_list.index(group) == len(data_list) - 1:
            dataSum += newGroup[-1]
            volumeDenom += volume
            average = str(round(dataSum / volumeDenom, 2))
            monthly_average_list.append((average, monthyear[5:7] + '-' + monthyear[0:4]))
        # if we're still in the same month, keep a running total of
        # the day's total sales and another running total of the volumes
        elif date[0:7] == monthyear:
            dataSum += newGroup[-1]
            volumeDenom += volume
        # if it's a new month, calculate the average using the running
        # totals for the previous month.  Add those to monthly_average_list.
        # set running total variables back to zero.  Set monthyear equal to the
        # new month and year.
        else:
            average = str(round(dataSum / volumeDenom, 2))
            monthly_average_list.append((average, monthyear[5:7] + '-' + monthyear[0:4]))
            monthyear = date[0:7]
            dataSum = newGroup[-1]
            volumeDenom = volume
    return monthly_average_list

# print the top 6 and bottom 6 months for Google stock
def print_info(monthly_average_list):
    monthly_average_list.sort()
    count = 0
    averageFile = open('monthly_averages.txt', 'w')
    
    bestMonths = monthly_average_list[-1:-7:-1]
    worstMonths = monthly_average_list[0:6]

    averageFile.writelines('6 best months for Google stock:\n')

    for myTup in bestMonths:
        averageFile.writelines(myTup[1] + ", " +  myTup[0] + '\n')

    averageFile.writelines('\n6 worst months for Google stock:\n')

    for myTup in worstMonths:
        averageFile.writelines(myTup[1] + ", " + myTup[0] + '\n')

    averageFile.close()
    
    return



data_list = get_data_list(stocksFile)
monthly_average_list = get_monthly_averages(data_list)
print_info(monthly_average_list)
stocksFile.close()
