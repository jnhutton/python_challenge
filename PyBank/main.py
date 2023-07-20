import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

profit_loss = []
monthly_change = []
date = []
 
count = 0
total_profit_loss = 0
total_change_profit_loss = 0
start_profit_loss = 0

# Open the CSV using the set path 
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
      count = count + 1 

      date.append(row[0])

      # Append the profit/loss and calculate the total profit/losses
      profit_loss.append(row[1])
      total_profit_loss = total_profit_loss + int(row[1])

      # Calculate the average monthly change in profit/losses. 
      # Then calulate the average change in profit/losses.
      end_profit_loss = int(row[1])
      monthly_change_profit_loss = end_profit_loss - start_profit_loss

      # Store the monthly change
      monthly_change.append(monthly_change_profit_loss)

      total_change_profit_loss = total_change_profit_loss + monthly_change_profit_loss
      start_profit_loss = end_profit_loss

      # Calculate the average change in profit/losses
      average_change_profit_loss = (total_change_profit_loss/count)
      
      # Identify the maxumim and the minimum monthly change in profit/losses 
      # Also, the dates where the maximum and minimum changes occurred
      greatest_increase_profit_loss = max(monthly_change)
      greatest_decrease_profit_loss = min(monthly_change)

      greatest_increase_date = date[monthly_change.index(greatest_increase_profit_loss)]
      greatest_decrease_date = date[monthly_change.index(greatest_decrease_profit_loss)]
    
    # Print out results
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(int(average_change_profit_loss)))
    print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profit_loss) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_profit_loss)+ ")")
    print("----------------------------------------------------------")

    # Create txt file of results
    f = open('analysis.txt', 'w')
    f.write("----------------------------------------------------------\n")
    f.write("Financial Analysis" + "\n")
    f.write("----------------------------------------------------------\n")
    f.write("Total Months: " + str(count) + "\n")
    f.write("Total Profits: " + "$" + str(total_profit_loss) +"\n")
    f.write("Average Change: " + '$' + str(int(average_change_profit_loss)) + "\n")
    f.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profit_loss) + ")\n")
    f.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_profit_loss) + ")\n")
    f.write("----------------------------------------------------------\n")
    f.close()