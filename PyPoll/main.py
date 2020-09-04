import os
import csv

#path to collect data
polling_csv = os.path.join('Resources','election_data.csv')

#read in the csv file
with open(polling_csv,'r') as csvfile:
    #split data on commas
    csvReader = csv.reader(csvfile, delimiter=',')
    header = next(csvReader)
    #print(f"File has been read")
    
    #initialize variables
    numVotes = 0
    canidateList = []
    voteCount = []
    votePercent = []
    
    for row in csvReader:
        #count the votes
        numVotes += 1
        
        if row[2] not in canidateList:
            #add canidate to the list
            canidateList.append(row[2])
            voteCount.append(0)
        
        #retrieve canidate index and increase voteCount
        index = canidateList.index(row[2])
        voteCount[index] = voteCount[index] + 1
    
    #do % calcuations
    for i in voteCount:
        votePercent.append("{:.3%}".format(i/numVotes))
        
    #find the winner
    winIndex = voteCount.index(max(voteCount))
    
    #data checking/printing
    print(f'Election Results')
    print(f'--------------------------')
    print(f'Total Votes: {numVotes}')
    print(f'--------------------------')
    #print(f'Winner index: {winIndex}')
    #print(f'{canidateList}\n{votePercent}\n{voteCount}')
    for results in range(len(canidateList)):
        print(f'{canidateList[results]}: {votePercent[results]} ({voteCount[results]})')
    print(f'--------------------------')
    print(f'Winner: {canidateList[winIndex]}')
    print(f'--------------------------')
    
#trying to create a new text file
exportFilepath = os.path.join('Analysis','PyPoll_analysis.txt')
f = open(exportFilepath,"w")
f.write(f'Election Results\n')
f.write(f'--------------------------\n')
f.write(f'Total Votes: {numVotes}\n')
f.write(f'--------------------------\n')
for results in range(len(canidateList)):
    f.write(f'{canidateList[results]}: {votePercent[results]} ({voteCount[results]})\n')
f.write(f'--------------------------\n')
f.write(f'Winner: {canidateList[winIndex]}\n')
f.write(f'--------------------------\n')
f.close()