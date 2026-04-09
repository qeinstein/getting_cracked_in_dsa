"""
Class 1 - Arrays & Complexity

This lesson file covers:
- Python list basics: append, indexing, slicing, and mixed values.
- A dynamic array with resize logic.

- LeetCode-style practice problems(We'll solve them later dw):
  - Two Sum
  - Best Time to Buy and Sell Stock
  - Longest Substring Without Repeating Characters

Run it with:
    python "First Class/arrays.py"
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


def python_list_basics() -> None: # THis is  simple function

    array = []  # This declares an empty Python list.
    array.append(3)  # append adds an item to the end, an integer.
    array.append(4)  # array is now [3, 4] after two appends.
    print("After appending integers:", array) # should print [3, 4]

    # Python lists can hold mixed data types(That is why we were able to add a string to the arr in today's class).
    # In lower-level languages like C and C++, arrays often store one data type only.
    array.append("python")
    print("After appending a string:", array) # will print it w the python
    
    # Indexing and Slicing
    numbers = [34, 7, 45, 36, 5, 55]

    first_value = numbers[0]  # 34
    first_five_values = numbers[0:5]  # [34, 7, 45, 36, 5]
    middle_values = numbers[1:3]  # [7, 45]

    print("First value:", first_value)
    print("numbers[0:5]:", first_five_values)
    print("numbers[1:3]:", middle_values)











def run_examples() -> None:
    """Run quick examples and sanity checks for the lesson."""

    print("Python list basics")
    python_list_basics()





if __name__ == "__main__":
    run_examples()


# If you have any questions feel free to use AI, if you still dont understand, then come to me
