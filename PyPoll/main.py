import os
import csv
import pandas as ps

# define path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv, store as dataframe
data_df = ps.read_csv(csvpath)

# count total number of votes
total_votes = data_df["Ballot ID"].count()

# count votes for each candidate and store as dataframe
counts_df = data_df["Candidate"].value_counts().to_frame()

# fix column names 
counts_df = counts_df.reset_index()
counts_df.columns = ["Name", "Votes"]

# find percentage each candidate received and store as column in dataframe
percent = round((counts_df["Votes"] / total_votes) * 100, 2)
counts_df["Percentage"] = percent

# print the analysis to console
print("Election Results")
print("-----------------")
print("Total Votes: "+str(total_votes))
print("-----------------")
for x in range(counts_df["Name"].count()):
    print(counts_df["Name"].iloc[x] + ": "+ str(counts_df["Percentage"].iloc[x]) + "% ("+ str(counts_df["Votes"].iloc[x]) + ")")
print("-----------------")
print("Winner: "+counts_df["Name"].iloc[0])
print("-----------------")

# print out results to txt file
txtpath = os.path.join('analysis', 'results.txt')
with open(txtpath, 'w') as f:
    f.write("Total Votes: "+str(total_votes))
    f.write('\n')
    for x in range(counts_df["Name"].count()):
        f.write(counts_df["Name"].iloc[x] + ": "+ str(counts_df["Percentage"].iloc[x]) + "% ("+ str(counts_df["Votes"].iloc[x]) + ")")
        f.write('\n')
    f.write("-----------------")
    f.write('\n')
    f.write("Winner: "+counts_df["Name"].iloc[0])