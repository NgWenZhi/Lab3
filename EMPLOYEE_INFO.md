
# Detailed Explanation of Employee Info Tracker Functions

This document explains the core functions from `employee_info.py` in a clear, beginner-friendly style—just like in our previous discussion.

---

## `calculate_average_salary()`

### Purpose:
Calculates the **average salary** of all employees in the `employee_data` list.

### How it works:
```python
total = 0
average = 0
```
- Initializes two variables: `total` to sum salaries, and `average` to store the final result.

```python
for eachDict in employee_data:
    emp_salary = eachDict["salary"]
    total += emp_salary
```
- Loops through each employee dictionary.
- Retrieves each salary and adds it to the `total`.

```python
average = total / len(employee_data)
average = round(average, 2)
```
- Divides the total salary by the number of employees (`len(employee_data)`).
- Rounds the result to 2 decimal places.

```python
return average
```
- Returns the average salary.

---

## `display_all_records()`

### Purpose:
Displays all employee records in a **neatly formatted table**.

### How it works:
```python
print(("Name" + "\t" +"Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
```
- Prints a header row using tab characters (`\t`) for spacing.
- `expandtabs(15)` makes sure columns are aligned.

```python
for item in employee_data:
    print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))
```
- Loops through all employees and prints their details in aligned columns.

---

## `get_employees_by_age_range(age_lower_limit, age_upper_limit)`

### Purpose:
Returns a list of employees whose ages fall **between** the specified lower and upper limits (exclusive).

### How it works:
```python
result = []
for item in employee_data:
    if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
        result.append(item)
```
- Converts ages and limits to integers.
- Checks if the employee's age is strictly **greater than** the lower limit and **less than** the upper limit.
- If true, adds the employee to the result list.

```python
return result
```
- Returns the filtered list.

---

## `get_employees_by_dept(department)`

###  Purpose:
Filters and returns employees who belong to the **specified department**.

### How it works:
```python
result = []
for eachDict in employee_data:
    emp_dept = eachDict["department"]
    if emp_dept == department:
        result.append(eachDict)
```
- Loops through each employee record.
- If the department matches, the employee is added to the result.

```python
return result
```
- Returns the filtered list.

---

## `display_records(employee_info)`

### Purpose:
Displays a given list of employee records (usually filtered).

### How it works:
- Similar to `display_all_records()`, but instead of the full list, it prints only the passed-in `employee_info`.

---

## `display_main_menu()`

### Purpose:
Displays a user-friendly menu and reacts based on the user’s input.

### Options it provides:
```
1 - Display all records
2 - Display average salary
3 - Display employee within age range
4 - Display employee in a department
Q - Quit
```

- Uses `input()` to get the user's choice and then calls the relevant function.

---

## `main()`

### Purpose:
Keeps the program running in a loop until the user chooses to quit.

### How it works:
```python
while (True):
    display_main_menu()
```
- Runs the main menu over and over until the program is manually exited.

---
