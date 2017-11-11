import os
import csv
totalMonth = 0
totalRevenue = 0
preRev = 0
totalChange = 0
averageChange = 0
maxValue = 0
maxIncrease = 0
minDecrease = 0
maxDate = ""
minDate = ""


# Open budget_data_1.cs\
with open("raw_data\\budget_data_1.csv", 'r') as budget:
    csvReader =csv.DictReader(budget)
    
# Open budget_data_2.csv
     #with open(budget_data_2.csv, 'r') as csvFile:
     #csvReader = csv.reader(csvFile, delimiter=',')

    for row in csvReader:
        totalMonth += 1
        totalRevenue += int(row ['Revenue'])
        changeRevenue =  int (row ['Revenue'])- preRev
        preRev = int(row ['Revenue'])		
        totalChange += changeRevenue
        if changeRevenue > maxIncrease:
            maxDate = row['Date']
            maxIncrease = changeRevenue
        if changeRevenue < minDecrease:
            minDate = row['Date']
            minDecrease = changeRevenue
    averageChange = (totalChange/totalMonth)		
    print ("Financial Analysis")
    print ("-------------------------------")	
    print ("Total Months :", totalMonth)
    print ("Total Revenue :", totalRevenue)
    print ("Average Revenue Change :", averageChange)
    print ("Greatest Increase in Revenue: ", maxDate, "($", maxIncrease, ")")
    print ("Greatest Decrease in Revenue:", minDate, "($", minDecrease, ")")
    

        
		
		
		