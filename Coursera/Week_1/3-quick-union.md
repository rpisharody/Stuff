## Quick-unon
Lazy approach to algorithm. Avoid working until necessary

#### Data Structure
* Integer array id[] of size N
* Interpretation: id[i] is parent of i
* Root of i is id[id[id[...id[i]...]]]

The array is a forest
Eg:
Index   : 0 1 2 3 4 5 6 7 8 9
Value   : 0 1 9 4 9 6 6 7 8 9

Find    : Check if p and q have the same root
Union   : To merge components containing p and q, set the id of p's root to id of q's root

```
public class QuickUnionUF {
    private int[] id;

    public QuickUnionUF(int N) {
        id = new int[N];
        for(int i = 0; i < N; i++) id[i] = i;
    }

    private int root(int i) {
        while ( i != id[i] )
            i = id[i];
        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int rp = root(p);
        int rq = root(q);
        id[rp] = rq;
    }
```

#### How efficient is the algorithm ?
Initialize  : N
Union       : N*
Find        : N
Because the tree can get too long, the worst case is N for find
