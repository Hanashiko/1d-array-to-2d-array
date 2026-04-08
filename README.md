# 1D Array to 2D Array

A Python solution for converting a one-dimensional array into a two-dimensional array with specified dimensions.

Based on [LeetCode 2022 - Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/).

## Usage

```bash
python main.py
```

## How it works

`construct2DArray(original, m, n)` takes a 1D list and reshapes it into an `m x n` 2D list. Returns an empty list if the dimensions don't match the original array length.

## Example

```python
construct2DArray([1, 2, 3, 4], m=2, n=2)
# [[1, 2], [3, 4]]

construct2DArray([1, 2], m=1, n=1)
# []
```
