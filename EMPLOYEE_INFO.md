# Explanation of Fruit Cost Calculator

This document explains the core functions used to compute the cost of fruits using `price_list` and `quantity_list`.

---

## Data Setup

Two dictionaries are defined at the top:

```python
price_list = {
    'apple' : 1.20,
    'orange': 1.40,
    'watermelon': 6.50,
    'pineapple': 2.70,
    'pear' : 0.90,
    'papaya': 2.95,
    'pomegranate': 4.95
}

quantity_list = {
    'apple': 5,
    'orange': 5,
    'watermelon': 1,
    'pineapple': 2,
    'pear' : 10,
    'papaya': 1,
    'pomegranate': 2
}
```

- `price_list` holds the price per fruit.
- `quantity_list` holds how many units of each fruit are being bought.

---

## `total_cost_shopping()`

### Purpose:
Calculates the total cost of all fruits in `quantity_list`.

### How it works:

```python
def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            price_per_piece = price_list[key]
            quantity = quantity_list[key]
            total_cost += (price_per_piece * quantity)

    print("total cost = ", total_cost)
    return total_cost
```

- Initializes `total_cost` to 0.
- Loops through all fruits in `price_list`.
- For each fruit, checks if it exists in `quantity_list`.
- Multiplies the unit price by the quantity and adds to the total.
- Prints and returns the final total cost.

---

## `cost_of_fruits(fruit, quantity)`

### Purpose:
Calculates the cost of buying a specific quantity of a given fruit.

### How it works:

```python
def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity * price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost
```

- Loops through the keys in `price_list`.
- If the fruit name matches the input, it calculates the cost.
- Cost is calculated by multiplying quantity with unit price.
- Prints and returns the result.

---

## `main()`

### Purpose:
Acts as the driver function to run and test the other functions.

### How it works:

```python
def main():
    cost_of_fruits('apple', 10)
    total_cost_shopping()
```

- Calls `cost_of_fruits()` to calculate the cost of 10 apples.
- Then calls `total_cost_shopping()` to compute the total cost of the full shopping list.

---

## Special Notes

- This code assumes fruit names are spelled correctly and exist in both dictionaries.
- If a fruit is not found in `price_list`, `cost_of_fruits()` will throw an error because `cost` would be undefined.
- For more robustness, a check should be added to handle fruits not in the dictionary.

