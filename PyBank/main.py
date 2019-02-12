import os
import csv

#Path to Ope the CSV
csvpath = os.path.join("Resources", "budget_data.csv")

# Create the variable (lists) to store the information requested
TotalNumberMonths = []
NetProfitLosses = []
ChangeProfitLosses = []

# Open the spreadsheet budget_data.csv .

with open(csvpath,newline="", encoding="utf-8") as budget_data:

   # Store the data of budget_data.csv
  csvreader = csv.reader(budget_data,delimiter=",")

  # Remove the header so we will only work with values
  header = next(csvreader)

  # Iterate through rows to fill our empty created Lists above.
  for row in csvreader:

      TotalNumberMonths.append(row[0])
      NetProfitLosses.append(int(row[1]))

  # Iterate through the profit_losses list created  to get the monthly change
  # (use -1 to calculate inside the loop the total_profit_losses[i+1] )

  for i in range(len(NetProfitLosses)-1):

      # Calculate the difference between two months and append the results in monthly profit change
      ChangeProfitLosses.append(NetProfitLosses[i+1]-NetProfitLosses[i])

# Obtain The greatest increase in profits (date and amount) over the entire period
MaxValue = max(ChangeProfitLosses)
MaxMonth = ChangeProfitLosses.index(max(ChangeProfitLosses)) + 1
# Obtain The greatest decrease in profits (date and amount) over the entire period
MinValue = min(ChangeProfitLosses)
MinMonth = ChangeProfitLosses.index(min(ChangeProfitLosses)) + 1

# Print with the results 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(TotalNumberMonths)}")
print(f"Total: $ {sum(NetProfitLosses)}")
print(f"Average Change: {round(sum(ChangeProfitLosses)/len(ChangeProfitLosses),2)}")
print(f"Greatest Increase in Profits: {TotalNumberMonths[MaxMonth]} $ ({(str(MaxValue))})")
print(f"Greatest Decrease in Profits: {TotalNumberMonths[MinMonth]} $ ({(str(MinValue))})")