### Union Find Algorithm
These are a class of algorithms that help us to solve the so called dynamic connectivity problem. 

What are the steps to solve a problem ?
* Model the problem
* Find a first pass algorithm to solve
* Is is fast enough ? Is it memory intensive ?
* Improve upon the algorithm
* Rinse and Repeat

#### Dynamic Connectivity
Given a set of N objects, we have a 'Union' command which connects any two points. The key question is then the 'Find/connected' query which tells if any two points are connected.

#### Modelling the connections
* 'is connected to' is a equivalence relation
* Reflexive : p is connected to p
* Symmetric : p -> q; then q -> p
* Transitive : p -> q; q -> r then p -> r
Use connected components as the superset of elements that are connected. We will use this database to efficiently answer if two elements are connected.


#### Union-find data type (API)
```
public class UF
UF (int N)                          // Init UF data structure with N objects
void union(int p, int q)            // add connection between nodes p and q
boolean connected (int p, int q)    // are p and q the same component ?
```


