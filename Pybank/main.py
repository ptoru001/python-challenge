import os
import csv
#/Users/alfonsotoruno/bootcamphw/python-challenge/Pybank/Resources/budget_data.csv
budgetdata = os.path.join("Pybank","Resources","budget_data.csv")
totalmonth = 0
#'open file'

with open(budgetdata) as budget:
    reader = csv.reader(budget)

    #'read the first row'


    header = next(reader) 

    for row in reader:
        totalmonth = totalmonth +1 

print(totalmonth)
