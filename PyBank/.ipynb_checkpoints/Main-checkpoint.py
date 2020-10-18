{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "--------------------------------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578.0\n",
      "Average Change:$-2315.12\n",
      "Greatest increase in profit: $1926159.0\n",
      "Greatst decrease in profit: $-2196167.0\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "import autopep8\n",
    "\n",
    "# Collect data from the Resources folder\n",
    "bank_csv = 'Resources/budget_data.csv'\n",
    "\n",
    "# Determine variables and lists\n",
    "total_months = []\n",
    "profit_loss = []\n",
    "change_profit_loss = []\n",
    "diff = 0\n",
    "net_total = 0\n",
    "\n",
    "# Read in the CSV file\n",
    "with open(bank_csv) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    header = next(csvreader)\n",
    "\n",
    "    # Calculate the total number of months included in the dataset (each row has one month)\n",
    "    for row in csvreader:\n",
    "        total_months.append(row[0])\n",
    "        profit_loss.append(float(row[1]))\n",
    "\n",
    "    # Calculate the average of the changes in Profit/Loss over the entire period\n",
    "    for i in range(1, len(profit_loss)):\n",
    "        change_profit_loss.append(profit_loss[i] - profit_loss[i-1])\n",
    "        average_change = sum(change_profit_loss)/len(change_profit_loss)\n",
    "        greatest_profit = max(change_profit_loss)\n",
    "        greatest_loss = min(change_profit_loss)\n",
    "\n",
    "    # Calculate the net total amt of Profit/Losses over the entire period\n",
    "    net_total = sum(profit_loss)\n",
    "\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"-------------------------\"*2)\n",
    "    print(f'Total Months: {len(Total_months)}')\n",
    "    print(f'Total: ${net_total}')\n",
    "    print(f'Average Change:${round(average_change,2)}')\n",
    "\n",
    "    # Calculate the greatest increase in profit\n",
    "    print(f'Greatest increase in profit: ${greatest_profit}')\n",
    "\n",
    "    # Calculate the greatest decrease in Profit\n",
    "    print(f'Greatst decrease in profit: ${greatest_loss}')\n",
    "\n",
    "# Set variable for output file\n",
    "output_file = (\"Analysis/PyBank_final.txt\")\n",
    "\n",
    "#  Open the output file\n",
    "with open(output_file, \"w\") as datafile:\n",
    "    writer = csv.writer(datafile)\n",
    "\n",
    "    # Write the rows\n",
    "    writer.writerow(['Financial Analysis'])\n",
    "    writer.writerow(['-----------------------'*2])\n",
    "    writer.writerow([f'Total Months: {len(Total_months)}'])\n",
    "    writer.writerow([f'Total: ${net_total}'])\n",
    "    writer.writerow([f'Average Change:${round(average_change,2)}'])\n",
    "    writer.writerow([f'Greatest increase in profit: ${greatest_profit}'])\n",
    "    writer.writerow([f'Greatst decrease in profit: ${greatest_loss}'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
