import os
import csv

#path to collect data from the resources folder
banking_csv = os.path.join('Resources','budget_data.csv')

#read in the csv file
with open(banking_csv,'r') as csvfile:
    #split data on commas
    csvReader = csv.reader(csvfile, delimiter=',')
    header = next(csvReader)
    #print(f"File has been read")
    
    #initialize variables
    numMonths = 0
    netTotal = 0
    currVal = 0
    deltaList = []
    greatIncrease = 0
    greatDecrease = 0

    for row in csvReader:
        numMonths += 1
        netTotal = netTotal + int(row[1])
        prevVal = currVal
        currVal = int(row[1])
        delta = currVal-prevVal
        deltaList.append(delta)
        
        #find the greatest increase in profits
        if delta > greatIncrease:
            greatIncrease = delta
            greatIncrMY = row[0]
        #find the greatest decrease in profits
        if delta < greatDecrease:
            greatDecrease = delta
            greatDecrMY = row[0]
    
    #remove the first index of delta list (no change from prior)
    deltaList.pop(0)
    avgDelta = sum(deltaList)/len(deltaList)
    #fix formatting
    netTotal = "${:,.0f}".format(netTotal)
    avgDelta = "${:,.2f}".format(avgDelta)
    greatIncrease = "${:,.0f}".format(greatIncrease)
    greatDecrease = "${:,.0f}".format(greatDecrease)
    
    #data checking/printing
    print(f'Financial Analysis')
    print(f'-------------------------')
    print(f'Total Months: {numMonths}') #correct answer = 86
    print(f'Total: {netTotal}') #correct answer = $38382578
    #print(f'The delta list is {deltaList}')
    print(f'Average Change: {avgDelta}') #correct answer = $-2315.12
    print(f'Greatest Increase in Profits: {greatIncrMY} ({greatIncrease})') #correct answer = Feb-2012 ($1926159)
    print(f'Greatest Decrease in Profits: {greatDecrMY} ({greatDecrease})') #correct answer = Sep-2013 ($-2196167)
    
#trying to create a new text file
exportFilepath = os.path.join('Analysis','PyBank_analysis.txt')
f = open(exportFilepath,"w")
f.write('Financial Analysis\n')
f.write(f'-------------------------\n')
f.write(f'Total Months: {numMonths}\n') #correct answer = 86
f.write(f'Total: {netTotal}\n') #correct answer = $38382578
#print(f'The delta list is {deltaList}\n')
f.write(f'Average Change: {avgDelta}\n') #correct answer = $-2315.12
f.write(f'Greatest Increase in Profits: {greatIncrMY} ({greatIncrease})\n') #correct answer = Feb-2012 ($1926159)
f.write(f'Greatest Decrease in Profits: {greatDecrMY} ({greatDecrease})\n') #correct answer = Sep-2013 ($-2196167)
f.close()