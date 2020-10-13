import os
import csv

#Setting a path to collect data from the Resource folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Setting a path to a text file with analysis results
budget_analysis_txt = os.path.join("Analysis", "budget_analysis.txt")
# Setting initial count for amount of months
month_count = 0

# Setting initial count for profit/losses
profit_total = 0

#Setting initial count for last month`s profit
profit_last_month = 0

#Setting a list for storage months
month_list = []

# Setting a list for storage values of changes from month to month
profit_changes_list = []

#Setting a function for counting an average
def average():
    average_change = sum(profit_changes_list)/len(profit_changes_list)
    return(average_change)
# Reading through CVS file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skipping header
    header = next(csvreader)
    
    # Loop through the data and counting months and profit/losses
    
    for row in csvreader:
        #Counting total months 
        month_count += 1
        #Converting Profit/losses data to float
        profit_current_month = float(row[1])
        #Counting total Profit/Losses
        profit_total += profit_current_month
        
        #Excluding first month
        if month_count >= 2:
            profit_changes_list.append(profit_current_month - profit_last_month)
            month_list.append(str(row[0]))
                
        profit_last_month = profit_current_month
    #Calling for the function
    average_change = average()      
#Writing results in a new text file and printing results in the terminal
with open(budget_analysis_txt, "w") as writer:  
    
    print("Financial Analysis")
    writer.writelines("Financial Analysis\n")
    print(f"Total month: {month_count}.")
    writer.writelines(f"Total month: {month_count}.\n")
    print(f"Total profit: ${profit_total}.")
    writer.writelines(f"Total profit: ${profit_total}.\n")
    print(f"Averenge change in Profit/losses: ${average_change}.")
    writer.writelines(f"Averenge change in Profit/losses: ${average_change}.\n")
    
    #Counting max and min values for analysis
    max_increase = max(profit_changes_list)
    max_decrease = min(profit_changes_list)
    
    #Setting a dictionary
    profit_keys = profit_changes_list
    month_values = month_list
    dictionary = dict(zip(profit_keys, month_values))
    #Writing results in a new text file and printing results in the terminal
    print(f"Greatest increase in Profits: {dictionary[max_increase]}, ${max_increase}.")    
    writer.writelines(f"Greatest increase in Profits: {dictionary[max_increase]}, ${max_increase}.\n")
    print(f"Greatest decrease in Profits: {dictionary[max_decrease]}, ${max_decrease}.")
    writer.writelines(f"Greatest decrease in Profits: {dictionary[max_decrease]}, ${max_decrease}.")
    

    
