# Stacks and Queues

Fundamental datatypes
* Value : Collection of objects
* Operations: insert, remove, iterate, test if empty

Stack: Take out the item most recently added - LIFO - push, pop
Queue: Least recently added - enqueue, dequeue - FIFO discipline

### Modular Programming
Seperate implementation and interface. Allows code reuse. Modular reusable libraries. Allows us to focus on performance. 

### Stacks
The API:
* StackOfStrings()  -> Create empty stack
* push(item)        -> insert a new string onto the stack
* pop()             -> pop the most recently added
* isEmpty()         -> boolean. is the Stack empty ?

```
# Test Client
import sys
import Stack
s = Stack.StackOfStrings()

while line is sys.stdin.readline().split():
    if line == '-':
        print(s.pop())
    else:
        s.push(line)
```
