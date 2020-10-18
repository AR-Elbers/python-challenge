import os
import csv
import autopep8

# Collect data from the Resources folder
bank_csv = 'Resources/budget_data.csv'

# Determine variables and lists
total_months = []
profit_loss = []
change_profit_loss = []
diff = 0
net_total = 0

# Read in the CSV file
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Calculate the total number of months included in the dataset (each row has one month)
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(float(row[1]))

    # Calculate the average of the changes in Profit/Loss over the entire period
    for i in range(1, len(profit_loss)):
        change_profit_loss.append(profit_loss[i] - profit_loss[i-1])
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        greatest_profit = max(change_profit_loss)
        greatest_loss = min(change_profit_loss)

    # Calculate the net total amt of Profit/Losses over the entire period
    net_total = sum(profit_loss)

    print("Financial Analysis")
    print("-------------------------"*2)
    print(f'Total Months: {len(Total_months)}')
    print(f'Total: ${net_total}')
    print(f'Average Change:${round(average_change,2)}')

    # Calculate the greatest increase in profit
    print(f'Greatest increase in profit: ${greatest_profit}')

    # Calculate the greatest decrease in Profit
    print(f'Greatst decrease in profit: ${greatest_loss}')

# Set variable for output file
output_file = ("Analysis/PyBank_final.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the rows
    writer.writerow(['Financial Analysis'])
    writer.writerow(['-----------------------'*2])
    writer.writerow([f'Total Months: {len(Total_months)}'])
    writer.writerow([f'Total: ${net_total}'])
    writer.writerow([f'Average Change:${round(average_change,2)}'])
    writer.writerow([f'Greatest increase in profit: ${greatest_profit}'])
    writer.writerow([f'Greatst decrease in profit: ${greatest_loss}'])