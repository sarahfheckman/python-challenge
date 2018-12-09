import os
import csv

#read in the csv file
read_file = os.path.join("C:/Users/sarah/Desktop/SMDA201811DATA2/02-Homework/03-Python/ExtraContent/Instructions/PyBoss/employee_data.csv")
with open(read_file, newline='') as csvfile:
    employee_data = csv.reader(csvfile, delimiter=',')
    print(employee_data)


