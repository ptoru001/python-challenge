import os
import csv
#/Users/alfonsotoruno/bootcamphw/python-challenge/Pybank/Resources/budget_data.csv
budgetdata = os.path.join("Pybank","Resources","budget_data.csv")
output_file = os.path.join("Pybank","Resources","budget_analysis.txt") 
totalmonth = 0
Total = 0
AverageChange = 0
Increase = 0 
Decrease = 0
#'open file'

with open(budgetdata) as budget:
    reader = csv.reader(budget)

    #'read the first row'


    header = next(reader) 

    for row in reader:
        totalmonth = totalmonth +1 

# save to output file 

output = (
    f'Financial Analysis\n'
    f'--------------------\n'
    f'Total Months: {totalmonth}\n'
    f'Total: {Total}\n'
    f'Average change: {AverageChange}\n'
    f'Greatest Increase: {Increase}\n'
    f'Greatest Decrease: {Decrease}\n')
    

print(output)

with open(output_file, 'w') as txt_file:
    txt_file.write(output)

