{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Election Results\n",
      "---------------------\n",
      "Total Votes: 3521001\n",
      "---------------------\n",
      "---------------------\n",
      "Winner: Khan\n",
      "---------------------\n",
      "---------------------\n",
      "Individual Candidate Results\n",
      "---------------------\n",
      "\n",
      "Khan:63.0% (2218231)\n",
      "Correy:20.0% (704200)\n",
      "Li:14.0% (492940)\n",
      "O'Tooley:3.0% (105630)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "import autopep8\n",
    "\n",
    "# Path to collect data from the Resources folder\n",
    "PyPoll_csv = ('Resources/election_data.csv')\n",
    "\n",
    "# declare lists etc\n",
    "Candidates = []\n",
    "Total_voters = []\n",
    "count = 0\n",
    "Total_votes = []\n",
    "percent_votes = []\n",
    "candidate_percent = []\n",
    "highest_index = 0\n",
    "\n",
    "# Read in the CSV file\n",
    "with open(PyPoll_csv) as csvfile:\n",
    "\n",
    "    # Split the data on commas\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    header = next(csvreader)\n",
    "\n",
    "    # Loop through the data\n",
    "    for row in csvreader:\n",
    "        # Calculate the total number of voters\n",
    "        Total_voters.append(row[0])\n",
    "\n",
    "        # Calculate the list of Candidates who received votes and total votes each candidate won\n",
    "        candidate = row[2]\n",
    "        if candidate in Candidates:\n",
    "            candidate_index = Candidates.index(candidate)\n",
    "            Total_votes[candidate_index] = Total_votes[candidate_index] + 1\n",
    "        else:\n",
    "            Candidates.append(candidate)\n",
    "            Total_votes.append(1)\n",
    "\n",
    "    # Calculate the % votes for each candidate\n",
    "    highest_count = Total_votes[0]\n",
    "    for i in range(len(Candidates)):\n",
    "        percent_votes = round((Total_votes[i]/len(Total_voters))*100, 3)\n",
    "        candidate_percent.append(percent_votes)\n",
    "    # Calculate the Winner\n",
    "        if Total_votes[i] > highest_count:\n",
    "            highest_count = Total_votes[i]\n",
    "            highest_index = i\n",
    "\n",
    "total_votes = len(Total_voters)\n",
    "winner = Candidates[highest_index]\n",
    "\n",
    "\n",
    "output = (\n",
    "    f\"\\nElection Results\\n\"\n",
    "    f\"---------------------\\n\"\n",
    "    f\"Total Votes: {total_votes}\\n\"\n",
    "    f\"---------------------\\n\"\n",
    "    f\"---------------------\\n\"\n",
    "    f\"Winner: {winner}\\n\"\n",
    "    f\"---------------------\\n\"\n",
    "    f\"---------------------\\n\"\n",
    "    f\"Individual Candidate Results\\n\"\n",
    "    f\"---------------------\\n\")\n",
    "print(output)\n",
    "\n",
    "for i in range(len(Candidates)):\n",
    "    output1 = f\"{Candidates[i]}:{candidate_percent[i]}% ({Total_votes[i]})\"\n",
    "    print(output1)\n",
    "\n",
    "# Set variable for output file\n",
    "output_file = (\"Analysis/PyPoll_final.txt\")\n",
    "\n",
    "with open(output_file, \"a\") as txt_file:\n",
    "    txt_file.write(output)\n",
    "    for i in range(len(Candidates)):\n",
    "        output3 = f\"{Candidates[i]}:{candidate_percent[i]}% ({Total_votes[i]})\\n\"\n",
    "        txt_file.write(output3)"
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