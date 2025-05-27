# Explanation of Bubble Sort with Unit Testing Setup

This document provides a detailed explanation of the bubble sort implementation used in the `Lab 3 - Software Unit Testing with PyTest`.

---

## Constants

```python
SORT_ASCENDING = 0
SORT_DESCENDING = 1
```
- Constants used to define the sorting order:
  - `0` means sort in ascending order.
  - `1` means sort in descending order.

---

## `bubble_sort(arr, sorting_order)`

### Purpose:
Sorts a list using the **bubble sort algorithm**, with options for ascending or descending order.

---

### How it works:

```python
arr_result = arr.copy()
```
- Makes a copy of the original list to avoid modifying it directly.

```python
n = len(arr_result)
```
- Gets the number of elements in the array.

---

### Limitation:
```python
if n < 10:
```
- Sorting only proceeds if the list has **fewer than 10 items**.
- If there are 10 or more items, `arr_result` is set to `-1`.

---

### Bubble Sort Logic:

```python
for i in range(n - 1):
    for j in range(0, n - i - 1):
```
- Outer loop: controls passes through the list.
- Inner loop: compares adjacent elements and swaps if needed.

---

### Ascending Sort:
```python
if sorting_order == SORT_ASCENDING:
    if arr_result[j] > arr_result[j + 1]:
        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
```
- If the current element is **greater than** the next, swap them.

---

### Descending Sort:
```python
elif sorting_order == SORT_DESCENDING:
    if arr_result[j] < arr_result[j + 1]:
        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
```
- If the current element is **less than** the next, swap them.

---

### Invalid Order:
```python
else:
    arr_result = []
```
- If the sorting order is not `0` or `1`, return an **empty list**.

---

### Final Result:
```python
return arr_result
```
- Returns the sorted list (or `-1` if too large, or `[]` if invalid order).

---

## `main()` Function

### Purpose:
Demonstrates sorting a sample list in both ascending and descending order.

```python
arr = [64, 34, 25, 12, 22, 11, 90]
```

```python
result = bubble_sort(arr, SORT_ASCENDING)
print(result)
```
- Prints the list sorted in ascending order.

```python
result = bubble_sort(arr, SORT_DESCENDING)
print(result)
```
- Prints the list sorted in descending order.

---

## 
Special Notes

- If the list has 10 or more elements, it will return `-1`.
- This limitation could be useful for testing conditions with invalid input sizes.

---
