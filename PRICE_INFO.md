# Explanation of Fruit Cost Calculator

This document explains the core functions used to compute the cost of fruits using `price_list` and `quantity_list`.

---

## Data Setup

Two dictionaries are used:

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

- price_list holds the unit price of each fruit.
- quantity_list holds how many units of each fruit are being bought.

---

## total_cost_shopping()

Purpose:
Calculates the total cost of all fruits in the quantity list.

How it works:
1. Initializes total_cost to 0.
2. Loops through all fruits in price_list:
   for key in price_list.keys()
3. Checks if the fruit exists in quantity_list:
   if key in quantity_list
4. Retrieves the unit price and quantity:
   price_per_piece = price_list[key]
   quantity = quantity_list[key]
5. Multiplies price by quantity and adds to total_cost:
   total_cost += (price_per_piece * quantity)
6. Prints and returns the total cost.

---

## cost_of_fruits(fruit, quantity)

Purpose:
Calculates and returns the cost of buying a specific quantity of a single fruit.

How it works:
1. Loops through the price_list keys:
   for key in price_list.keys()
2. If the fruit matches the input:
   if key == fruit
3. Calculates the cost by multiplying quantity with unit price:
   cost = quantity * price_list[key]
4. Breaks the loop once the match is found.
5. Prints and returns the cost.

---

## main()

Purpose:
Serves as the driver function to test the above two functions.

Steps:
1. Calls cost_of_fruits('apple', 10)
   - Calculates the cost of 10 apples.
2. Calls total_cost_shopping()
   - Calculates the total cost of all fruits in the quantity list.

---

## Special Notes

- This code assumes all fruit names used are spelled exactly as they appear in the dictionaries.
- No error handling is done for fruits that are not in the price list.
- If a fruit is not found, cost_of_fruits() would fail because `cost` would be undefined.
  (A default value or error check could be added for robustness.)
  
