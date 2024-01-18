## PyBank

# Importing dependencies

import os
import csv

# Setting file path

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# Opening and reading csv file

with open(budget_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    # Reading and storing the header row first
    
    csv_header = next(csv_file)
    
    # Setting requisite variables
    
    total_months = 0
    profit_losses = 0
    prev_profit_losses = None
    net_total_amount = 0
    change = 0
    changes = []
    average_change = 0
    greatest_increase = 0
    increase_date = None
    greatest_decrease = 0
    decrease_date = None
    
    # (For use of "None" see https://stackoverflow.com/questions/664294/is-it-possible-only-to-declare-a-variable-without-assigning-any-value-in-python)
    
    # Looking through each row in the csv file, increasing the month count, and increasing the net total amount (after changing data type from str to int)
    
    for row in csv_reader:
        total_months = total_months + 1
        profit_losses = int(row[1])
        net_total_amount = net_total_amount + profit_losses
        
        # Filling in the "changes" list with the month-to-month differences
        
        if prev_profit_losses != None:
            change = profit_losses - prev_profit_losses
            changes.append(change)
            
            # Finding the month with the greatest increase in profits and storing the amount
            
            if change > greatest_increase:
                greatest_increase = change
                increase_date = row[0]
            
            # Finding the month with the greatest decrease in profits and storing the amount    
            
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_date = row[0]
        
        # Setting the profits/losses for the next iteration of the for loop        
        
        prev_profit_losses = profit_losses
    
    # Finding the average month-to-month change in profits/losses    
    
    average_change = sum(changes) / (total_months - 1)
    
# Printing the desired results to the terminal
        
print(
      "Financial Analysis", "\n", "\n",
      "----------------------------", "\n", "\n",
      "Total Months: " + str(total_months), "\n", "\n",
      "Total: $" + str(net_total_amount), "\n", "\n",
      "Average Change: $" + str(round(average_change, 2)), "\n", "\n",
      "Greatest Increase in Profits: " + increase_date + " ($" + str(greatest_increase) + ")", "\n", "\n",
      "Greatest Decrease in Profits: " + decrease_date + " ($" + str(greatest_decrease) + ")"
      )

    # (For line break info, see https://stackoverflow.com/questions/5982206/how-to-print-a-linebreak-in-a-python-function)

# Setting the variable and path for the output file

output_path = os.path.join(".", "analysis", "budget_data_analysis.txt")

# Opening the output file

with open(output_path, "w") as output_file:
    
    # Writing the rows of the output file (see https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python)
    
    output_file.write("Financial Analysis""\n""\n")
    output_file.write("----------------------------""\n""\n")
    output_file.write(f"Total Months: {total_months}""\n""\n")
    output_file.write(f"Total: ${net_total_amount}""\n""\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}""\n""\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})""\n""\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})""\n""\n")