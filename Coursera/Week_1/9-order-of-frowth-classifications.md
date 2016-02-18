# Order of Growth Classifications

A Small set of functions:
1, log N, N, N log N, N^2, N^3, and 2^N

```
# Binary Search Algorithm
# Use sorted array for this

def binary_search(array, key):
    lo = 0
    hi = len(array) - 1
    while (lo <= hi):
        mid = lo + (hi - lo)/2
        if key < array[mid]:
            hi = mid - 1
        elif key > array[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
```

Proposition : Binary search uses atmost 1 + lg N compares to search in a sorted array of size N

Similarly, for the 3-sum problem, a N^2 lg N algorithm can be developed

Step 1:
    Sort the array (N^2 - insertion sort)
Step 2:
    For each pair (i, j) from the array, binary search for -(i+j) -> lg N
Thus the problem can be reduced to complexity of N^2 lg N
