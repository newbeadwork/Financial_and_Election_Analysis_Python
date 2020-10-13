import os
import csv

#Setting a path to collect data from the Resource folder
election_data_csv = os.path.join("Resources", "election_data.csv")

election_analysis_txt = os.path.join("Analysis", "election_analysis.txt")
#Setting initial total voters count
total_votes = 0

#Setting election results as a dictionary
election_results = dict()

#Setting a variable for choosing the election`s winner
max_percent = 0

#Defining a new function for counting votes inside the dictionary
def counting_votes(value, total_votes):
    #name = str(key)
    votes = len(value)
    percent = (votes/total_votes)* 100
    #print(f"{name}: {percent}% ({votes})")
    return(percent)
    
#Opening and looping trough csv file and creating dictionary with 
# candiddate names as keys and voters ID`s as values
with open(election_data_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)

    for row in csvreader:
        #Counting total votes
        total_votes += 1
        #Setting a variable for creating the dictionary
        candidate = row[2]
        #Filling the dictionary
        if candidate not in election_results:
            #Adding a new key
            election_results.setdefault(row[2], [])
            #Adding a new value
            election_results[row[2]].append(row[0]) 
        else:
            #Adding a new value to existing key
            election_results[row[2]].append(row[0])
with open(election_analysis_txt, "w") as writer:    
#Printing results
    print("Election Results")
    writer.writelines("Election Results\n")
    print(f"Total Votes: {total_votes}")
    writer.writelines(f"Total Votes: {total_votes}\n")

#Looping through the dictionary
    for key, value in election_results.items() :
    
    #Calling for function and defining a variable from this function
        percent = counting_votes(value, total_votes)
        print(f"{key}: {percent}% ({len(value)})")
        writer.writelines(f"{key}: {percent}% ({len(value)})\n")
    #Setting condition for choosing the biggest percent of votes
        if percent >= max_percent:
            max_percent = percent
            name = key
    print(f"Winner: {name}")
    writer.writelines(f"Winner: {name}\n")



    