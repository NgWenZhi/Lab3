# Lab 3 - Developing software Test Cases 



#  ET0735 Lab Test Quick Reference (Labs 1-3)

> Open-book friendly cheatsheet. Do **not** use ChatGPT during the test.

---

##  Python: Function Syntax & Examples

### Function Declaration
```python
def function_name(arg1, arg2):
    # your logic
    return result
```

### Example: BMI Calculator
```python
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return -1
    elif 18.5 <= bmi <= 25.0:
        return 0
    else:
        return 1
```

---

##  PyTest: Unit Testing

### Basic Test Case Example
```python
import your_module as mod

def test_some_function():
    result = mod.some_function(input)
    assert result == expected_output
```

### BMI Test Example
```python
import bmi

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.73, 50) == -1

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.73, 60) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.73, 80) == 1
```

---

##  Git Commands (Quick Use)

### Init, Add, Commit
```bash
git init
git add .
git commit -m "Initial commit"
```

### Connect to Remote
```bash
git remote add origin <repo_url>
git push -u origin master
```

### Set New Remote
```bash
git remote set-url origin <new_repo_url>
```

### Tags and Releases
```bash
git tag -a Lab3_v1.0 -m "Initial version"
git push origin Lab3_v1.0
```

### Submodule (for importing Lab 2 into Lab 3)
```bash
git submodule add <Lab2_repo_url>
```

---

##  Lab 2 Functions (Temperature Processing)

```python
def calc_average(lst):
    return sum(lst) / len(lst)

def find_min_max(lst):
    return [min(lst), max(lst)]

def sort_temperature(lst):
    return sorted(lst)

def calc_median_temperature(lst):
    lst.sort()
    n = len(lst)
    return lst[n//2] if n % 2 != 0 else (lst[n//2 - 1] + lst[n//2]) / 2
```

---

##  Lab 3: Dictionary Examples (price_info.py)

```python
price_list = {"apple": 2.5, "banana": 1.5}
quantity_list = {"apple": 3, "banana": 2}

def cost_of_fruit(fruit, quantity):
    return price_list[fruit] * quantity

def total_cost_shopping():
    total = 0
    for fruit in price_list:
        total += price_list[fruit] * quantity_list[fruit]
    return total
```

### PyTest for price_info
```python
import price_info

def test_cost_of_fruit():
    assert price_info.cost_of_fruit("apple", 2) == 5.0

def test_total_cost_shopping():
    assert price_info.total_cost_shopping() == 9.5
```

---

##  .gitignore
```bash
__pycache__/
```

---

##  Markdown Quick Syntax

### Headers
```markdown
# H1
## H2
### H3
```

### Code Block
\`\`\`python  
print("Hello")  
\`\`\`

### Lists
- Item 1
- Item 2

### Ordered List
1. First
2. Second

### Table
```markdown
| Feature       | Status |
| ------------- | ------ |
| BMI Test      | Correct|
| Price Module  | Correct|
```

---

##  Useful Links
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Python W3Schools](https://www.w3schools.com/python/)

---

---

##  Extended PyTest Unit Test Examples

###  Unit Tests for BMI Calculator (`bmi.py`)
```python
import bmi

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.75, 50) == -1  # BMI = 16.3

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.75, 70) == 0   # BMI = 22.86

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.75, 90) == 1   # BMI = 29.39
```

### Unit Tests for Lab 2 Temperature Functions
```python
import lab2

def test_calc_average():
    assert lab2.calc_average([1.0, 2.0, 3.0]) == 2.0

def test_find_min_max():
    assert lab2.find_min_max([10.5, 3.2, 7.0]) == [3.2, 10.5]

def test_sort_temperature():
    assert lab2.sort_temperature([5, 1, 3]) == [1, 3, 5]

def test_calc_median_temperature_odd():
    assert lab2.calc_median_temperature([5, 1, 3]) == 3

def test_calc_median_temperature_even():
    assert lab2.calc_median_temperature([1, 2, 3, 4]) == 2.5
```

### Unit Tests for Lab 3 Dictionary Functions (`price_info.py`)
```python
import price_info

def test_cost_of_fruit():
    assert price_info.cost_of_fruit("apple", 2) == 5.0  # 2.5 * 2

def test_total_cost_shopping():
    assert price_info.total_cost_shopping() == 9.5  # apple: 3*2.5 + banana: 2*1.5
```

### Unit Tests for Lab 3 Sorting Function (`Lab3.py`)
```python
import Lab3

def test_bubble_sort_ascending():
    assert Lab3.bubble_sort([4, 2, 1], Lab3.SORT_ASCENDING) == [1, 2, 4]

def test_bubble_sort_descending():
    assert Lab3.bubble_sort([4, 2, 1], Lab3.SORT_DESCENDING) == [4, 2, 1]

def test_bubble_sort_invalid_length():
    assert Lab3.bubble_sort(list(range(10)), Lab3.SORT_ASCENDING) == 1

def test_bubble_sort_empty():
    assert Lab3.bubble_sort([], Lab3.SORT_ASCENDING) == 0

def test_bubble_sort_non_integer():
    assert Lab3.bubble_sort(["a", "b"], Lab3.SORT_ASCENDING) == 2
```

---

---

## Git Branching & Tagging Commands

### Branch Management
```bash
# List branches
git branch

# Create new branch
git branch <branch_name>

# Switch to branch
git checkout <branch_name>

# Create and switch in one step
git checkout -b <branch_name>

# Merge a branch into current
git merge <branch_name>
```

### Tagging & Releases
```bash
# Create tag
git tag -a Lab3_v1.0 -m "Initial release"

# Push tag to remote
git push origin Lab3_v1.0

# List all tags
git tag
```

---

## How to Push This File to GitHub

### 1. Navigate to Your Local Repo Folder
```bash
cd C:/Local_Git_Repository/Lab3
```

### 2. Move the Markdown File
Copy `ET0735_Lab_Test_CheatSheet.md` into your Lab3 project folder.

### 3. Stage, Commit, and Push
```bash
git add ET0735_Lab_Test_CheatSheet.md
git commit -m "Add lab test cheatsheet"
git push origin master
```

### 4. Optional: Tag This Commit and Create a GitHub Release
```bash
git tag -a Lab3_v5.0 -m "Add full cheatsheet for lab test"
git push origin Lab3_v5.0
```

---

