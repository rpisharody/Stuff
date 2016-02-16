### Improvement 1
Weighting - Weighted Quick Union
Avoid putting the large tree under the smaller root
Keep track of number of objects in each tree.
Root of smaller tree is always linked to root of larger tree.
Smaller tree is always put lower to the larger tree

#### Data Structure
Same as a Quick-Union. But we maintain an additional array, sz[i]
to count the number of objects in the tree rooted at i

Find is still the same
```
return root(p) == root(q)
```

Union : Modify the quick-union to 
* Link root of smaller tree
* Update the sz[] array with the new number of elements

```
int rp = root(p)
int qp = root(q)
if (rp == qp) return;
if (sz[rp] >= sz[qp]) {
    id[qp] = rp;
    sz[rp] += sz[qp]
} else {
    id[rp] = qp;
    sz[qp] += sz[rp]
}
```

Running time is proportional to depth of p and q
Union takes constant time (if the roots are already known)

Depth of any node x is at most lg N.

Initialize      : N
Union           : lg N
Find            : lg N

Two trees, when are connected, worst case is both trees are of same size, which means, for each union, the depth of the node interested doubles. But this doubling can happen only lg N times (for size N). Thus, at worst, finding a root takes lg N operation (if the node is at the very end of two identical tree merges)

This is the only computationally difficult operation as checking if connected is comparing the roots (so total 2 lg N + 1 -> O(lg N))

Union includes finding roots of two trees + some constant operation. Again the complexity is only O(lg N)


### Can this algorithm be improved ?
Path Compression
While traversing down a path to find root, set each root to its grandparent
```
private int root(i) {
    while(i != id[i]) {
        id[i] = id[id[i]]
        i = id[i]
    }
    return i;
```
0 1 2 3 4 5 6 7 8 9
0 1 3 4 5 5 6 7 8 9
When looking for root of 2, we notice that it is connected to root of 3
Thus we know that whatever is the root of 3 is also the root of 2.
So instead of going through 3 to get to root, set root of 2 as the root of 3
This compresses, flattens the tree. And that is the idea here !!

Algorithm is called *Hopcroft-Ulman, Trojan*

No such linear algorithm to do the Quick-Union-Find.
But in practice, the WQUFPC is the closes we have !!

# Summary
Weighted Quick Union (with path compression) makes it possible to solve problems in dynamic connectivity analysis that otherwise could not be addressed.

Algorithm       Worst-Case Time
Quick-Find          M N
Quick-Union         M N
Weighted QU         N + M log N
QU + Path Compress  N + M log N
Weighted QU + PC    N + M lg* N

where lg* N is the iterative log function (number of times we must take logarithm of N to reach 1. In practice, this is usualy 5)
