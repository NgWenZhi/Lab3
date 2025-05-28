# Explanation of Employee Info Tracker

This document explains the key functions found in the `employee_info.py` file.

---

## `calculate_average_salary()`

### Purpose:
Computes the average salary of all employees in `employee_data`.

### How it works:

```python
def calculate_average_salary():
    total = 0
    average = 0
    for eachDict in employee_data:
        emp_salary = eachDict["salary"]
        total += emp_salary
    average = total / len(employee_data)
    average = round(average, 2)
    return average
```

- Initializes `total` to 0 to keep track of the salary sum.
- Loops through each employee dictionary to add up the salaries.
- Divides the total by the number of employees using `len(employee_data)`.
- Rounds the average to 2 decimal places before returning it.

---

## `display_all_records()`

### Purpose:
Displays all employee records in a clean tabular format.

### How it works:

```python
def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))
```

- Prints a header row with column labels.
- Loops through each dictionary in `employee_data` and prints the values with aligned tabs.

---

## `get_employees_by_age_range(age_lower_limit, age_upper_limit)`

### Purpose:
Returns a list of employees whose ages fall strictly between the given lower and upper limits.

### How it works:

```python
def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)
    return result
```

- Loops through all employee records.
- Converts the `age` and limits to integers for proper comparison.
- Checks if the age is strictly greater than the lower limit and less than the upper limit.
- Appends matching records to `result` and returns it.

### About the `int()` conversion:

The values are converted to integers because they may come from `input()` or a CSV file, which treats them as strings. Comparing strings numerically without converting can lead to incorrect results.

If the values are already integers, the `int()` conversion is unnecessary and could be skipped.

---

## `get_employees_by_dept(department)`

### Purpose:
Returns all employees that belong to a given department.

### How it works:

```python
def get_employees_by_dept(department):
    result = []
    for eachDict in employee_data:
        emp_dept = eachDict["department"]
        if emp_dept == department:
            result.append(eachDict)
    return result
```

- Iterates over each employee.
- Compares their department with the input.
- Appends matching employees to `result`.

---

## `display_records(employee_info)`

### Purpose:
Displays only the passed-in list of employee records in a tabular format.

### How it works:

```python
def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))
```

- Similar to `display_all_records()`, but it only prints the records passed into the function.

---

## `display_main_menu()`

### Purpose:
Displays a text-based menu and handles user interaction.

### How it works:

```python
def display_main_menu():
    print("\n----- Employee information Tracker -----")
    print("Select option\n")
    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()
    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))
    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Upper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)
    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)
    elif option == 'Q':
        quit()
```

- Prints a menu.
- Reads input from the user.
- Based on the option, calls the relevant function and displays the results.

---

## `main()`

### Purpose:
Keeps the application running until the user quits.

### How it works:

```python
def main():
    while (True):
        display_main_menu()
```

- Uses a `while True` loop to keep showing the main menu until the user chooses to quit the program.

