## Oservations

### Example - The 3-sum problem
If we have N distinct integers, how many triples sum to exactly zero ?

```
$> cat 8ints.txt
8
30 -40 -20 -10 40 0 10 5

$> python ThreeSum.py 8ints.txt
4
```
The problem is deeply realted to computational geometry. The algorithms which relate to graphical problems. 

#### Brute-force algorithm
```
def count(a):
    N = len(a)
    count = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count
```
With the triple-for-loop, the running time scales as N^3
Regression fits a stright line through the data points

