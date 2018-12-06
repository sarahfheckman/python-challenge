#PyBank
import os
import csv

#import pathway
pybankCSV = os.path.join("C:/Users/sarah/Desktop/SMDA201811DATA2-master/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")

#create lists to store information
months = []
profit_losses = []


#read file
with open(pybankCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    csv_header = next(csvfile)

#pull information out of csv & convert to pythonic lists
    for column in csvreader:
        months.append(column[0])
        profit_losses.append(column[1])
        
#calculate total number of months
total_months = len(months)

#calculate net profit; convert list of strings to integers
profit_losses = [int(x) for x in profit_losses]
net_profit = sum(profit_losses)

#calculate average change in profit/loss
average_change_list = [(x - y) for (x, y) in zip(profit_losses[1:], profit_losses[:-1])]
average_change = sum(average_change_list) / (total_months-1)

#determine greatest increase in profits (include the month)
greatest_profit = max(average_change_list)

#determine the month this occured
profit_month = months[average_change_list.index(greatest_profit) + 1]

#determine the greatest loss (include the month)
greatest_loss = min(average_change_list)

#determine the month this occured
loss_month = months[average_change_list.index(greatest_loss) + 1]

#print to the terminal
print("FINANCIAL ANALYSIS")
print("------------------------")
print('Total Months: ' + str(total_months))
print('Total: ' + '${:,.2f}'.format(average_change))
print('Greatest Increase in Profits: ' + profit_month + " " + '${:,.2f}'.format(greatest_profit))
print('Greatest Decrease in Profits: ' + loss_month + " " + '${:,.2f}'.format(greatest_loss))