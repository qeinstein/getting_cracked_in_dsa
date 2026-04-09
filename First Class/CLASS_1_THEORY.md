# Class 1 Theory - Arrays & Complexity

## Big O Notation

Big O describes how an algorithm grows as the input size grows. It focuses on the dominant growth rate instead of exact seconds.

If `n` is the input size:

- `O(1)` means constant time. The work does not grow with `n`.
- `O(log n)` means logarithmic time. The work grows slowly, like binary search.
- `O(n)` means linear time. The work grows directly with `n`.
- `O(n log n)` is common in efficient sorting algorithms like merge sort.
- `O(n^2)` means quadratic time. Nested loops over the same input often cause this.

Examples:

```python
numbers[0]          # O(1)
target in numbers   # O(n) for a normal list scan
```

## Time Complexity

Time complexity measures how the number of operations grows.

Example:

```python
def print_all(numbers):
    for number in numbers:
        print(number)
```

This is `O(n)` because if the list has 10 items, the loop runs 10 times. If it has 1,000 items, the loop runs 1,000 times.

## Space Complexity

Space complexity measures how much extra memory an algorithm uses.

Example:

```python
def copy_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number)

    return result
```

This is `O(n)` extra space because it creates another list with `n` items.

## Static Arrays

A static array has a fixed size. Once created, the amount of space cannot grow automatically.

Important points:

- Values are stored next to each other in memory.
- Index access is fast because the computer can calculate the address directly.
- Adding beyond the fixed capacity is not allowed unless you create a new larger array and copy the old values.

## Dynamic Arrays

A dynamic array can grow when it runs out of capacity.

Python's `list` is a dynamic array. When it becomes full, Python allocates a bigger backing array, copies the old values, and then continues.

Important points:

- Index access is still `O(1)`.
- Normal append is `O(1)`.
- Append during a resize is `O(n)` because old values must be copied.
- Over many appends, append is amortized `O(1)` because resizing does not happen every time.

## Memory Layout

Arrays store values in contiguous positions. That means the values are placed next to each other in memory.

For index access, the computer can calculate:

```text
address = start_address + index * item_size
```

That is why reading `numbers[3]` does not require scanning indices `0`, `1`, and `2`. It jumps straight to the right position.

## Two-Pointer Pattern

The two-pointer pattern uses two indices to move through data.

Common uses:

- Removing duplicates from a sorted array.
- Reversing an array.
- Finding pairs in a sorted array.
- Partitioning values.

For removing duplicates:

- `read` scans each value.
- `write` marks where the next unique value should be stored.

This gives `O(n)` time and `O(1)` extra space.

## Sliding Window Pattern

The sliding window pattern tracks a section of an array or string.

It is useful when the problem asks about:

- A subarray.
- A substring.
- A fixed-size range.
- The longest or shortest section that satisfies a rule.

For fixed-size maximum sum:

- Compute the first window sum.
- Slide right by adding the new value.
- Remove the old value that left the window.

This avoids recomputing every window from scratch, giving `O(n)` time.

## Patterns To Remember

- If you need direct index access, arrays are strong.
- If you need many inserts or deletes in the middle, arrays can be expensive because values must shift.
- Use two pointers when two positions can move through the data to avoid nested loops.
- Use sliding window when a problem asks about contiguous subarrays or substrings.
- Always ask for both time complexity and space complexity.

### Again, reach out if you have issues understanding, we'll still discuss them in the next class though