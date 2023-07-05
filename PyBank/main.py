import os
import csv
import pandas as ps

# define path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv, store as dataframe
data_df = ps.read_csv(csvpath)

# calculate total # of months and net total
total_months = data_df["Date"].count()
net_total = data_df["Profit/Losses"].sum()

# calculate change in profit for each month and find average
data_df["Profit/Losses Change"] = data_df["Profit/Losses"].diff()
average_change = data_df["Profit/Losses Change"].mean()

# find row with max change
maxrow = data_df["Profit/Losses Change"].idxmax()
max_date = data_df.loc[maxrow,"Date"]
max_value = data_df.loc[maxrow,"Profit/Losses Change"]

# find row with biggest loss
minrow = data_df["Profit/Losses Change"].idxmin()
min_date = data_df.loc[minrow,"Date"]
min_value = data_df.loc[minrow,"Profit/Losses Change"]

# print out results to terminal
print("Financial Analysis")
print("-------------------")
print("Total Months: "+str(total_months))
print("Total: $"+str(net_total))
print("Average Change: $"+str(average_change))
print("Greatest Increase in Profits: "+max_date+" ($"+str(max_value)+")")
print("Greatest Decrease in Profits: "+min_date+" ($"+str(min_value)+")")

