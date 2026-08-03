import csv
import json

# Read employee data from CSV

employees = []

with open("employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

# Read salary data from JSON

with open("salary.json", "r") as file:
    salary_data = json.load(file)

# Convert salary list to dictionary

salary_dict = {}

for item in salary_data:
    salary_dict[str(item["employee_id"])] = item["salary"]

print("PAYROLL REPORT")
print("-" * 50)

for employee in employees:

    emp_id = employee["employee_id"]

    if emp_id in salary_dict:

        salary = salary_dict[emp_id]

        print(
            emp_id,
            employee["name"],
            employee["department"],
            salary
        )

    else:

        print(
            emp_id,
            employee["name"],
            employee["department"],
            "Salary Record Missing"
        )
