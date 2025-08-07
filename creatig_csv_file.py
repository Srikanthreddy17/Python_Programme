import csv

#create a list of lists with 5 rows and 6 columns
data = [
    ["name", "city", "age", "dept"], # header row
    ["Alice", "New York", 30, "Engineering"],
    ["Bob", "Los Angeles", 25, "Marketing"],
    ["Charlie", "Chicago", 35, "Sales"],
    ["David", "Houston", 28, "Engineering"],
    ["Eve", "Phoenix", 22, "Marketing"],
    ["Frank", "San Francisco", 40, "Sales"]
]
with open("student_data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)