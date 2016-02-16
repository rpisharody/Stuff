## Quick Find
Eager algorithm to solve connectivity problem

#### Data Structure
* Integer array id[] of size N
* Interpretation: p and q are connected iff they have the same id

Find : check if p and q have same id
Union : Merge components containing p and q, change all entries whose id equals id[p] to id[q]

```
public class QuickFindUF {
    private int[] id;

    public QuickFindUF(int N) {
        id = new int[N]
        for(int ii = 0; ii < N; ii++)
            id[ii] = ii
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q]
    }

    public void union(int p, intq) {
        // At-most 2N + 2 array accesses
        old_id = id[p]
        new_id = id[q]
        for(int ii = 0; ii < id.length; ii++) {
            if (id[ii] == old_id)
                id[ii] = new_id
        }
    }
}
```

#### How effective is the algorithm ?
Initialize  : N
Find        : 1
Union       : N
If there are N union commands on N objects, it takes N^2 (quadratic) time
Reason, they do not scale. Well, you can see why !
