## Memory Management

- Stack Memory is destroyed once function call Ends.
- However , Heap memory is not destroyed automatically and cause issues such as
  1. Memory Leak
  2. Dangling Pointers

### Differences Between Memory Leaks and Dangling Pointers

Memory management issues can lead to serious problems in software applications. Two common issues are memory leaks and dangling pointers. Understanding the differences between them is crucial for writing reliable and efficient code.

| Aspect           | Memory Leak                                       | Dangling Pointer                                       |
| ---------------- | ------------------------------------------------- | ------------------------------------------------------ |
| **Definition**   | Memory that is allocated but not freed            | Pointer referencing memory that has been freed         |
| **Cause**        | Forgetting to release allocated memory            | Accessing memory after it has been freed               |
| **Consequences** | Gradual increase in memory usage, potential crash | Undefined behavior, potential crash or data corruption |
| **Resolution**   | Ensure all allocated memory is freed              | Reset pointers after freeing memory, avoid double-free |

In Languages such c, c++ we need to manage memory using malloc and deallooc. However, high level languages such as Java and Python have Garbage Collection Mechanism.

## Garbage Collection

The process of automatic deletion of unwanted or unused objects to free the memory is called garbage collection. It also frees the dead memory and reclaims back the block of memory no longer in use for further usage..

```
Garbage Collection Can help solve issues of Memory Leaks and Dangling Pointers.
```

Two Strategies to Implement Garbage Collection

1. Reference Counter
2. Generational Garbage Collection

### Reference Counting

A reference count, or the number of references that point to an object. When an object’s reference count reaches zero, it becomes un-referenceable and its memory can be freed up. References are Stored in Stack.

Cyclical reference, also known as a reference cycle or circular reference, occurs when a group of objects reference each other in a way that forms a closed loop, preventing them from being garbage collected. This can lead to memory leaks as the objects involved are not eligible for automatic memory reclamation since their reference counts never reach zero.

```
# Example of Cyclic Reference
x = []
x.append(x)
print(x)
```

<b> To Handle Cyclic References Generation Garbage Collection Strategy is helpful </b>

### Algoritms for Memory Management

<b> Mark and Sweep </b> - Mark Memory blocks which can be ready for Freeing up and sweep using below Algorithms.

1. Normal Sweeping - After deleting Marked Memory , Heap will have Fragmented Space, which may lead to out of Memory for new objects if the size of new object is large.
2. Sweeping with Compacting - After Deleting Memory, Fragmented memory is joined together allowing for more continuous Freed Memory.
3. Sweeping with Copying - Instead of Compacting, we Collect unmarked pieces and copy it in new regoin delete old block.

Depending on our requirement we can use either sweep with Compacting / Copying.

### Generation Garbage Collection

- Generation 0 identifies a newly created object that has never been marked for collection
- Generation 1 identifies an object that has survived a GC (marked for collection but not removed because there was sufficient heap space)
- Generation 2 identifies an object that has survived more than one sweep of the GC.

### Other Strategies

- Manual Garbage Collection (Time Based, Event Based)
- Forced Garbage Collection (Deleting Objects Manually and calling Garbage Collector Immediately)

https://www.geeksforgeeks.org/garbage-collection-python/

## Resources

- https://dev.to/karishmashukla/how-python-uses-garbage-collection-for-efficient-memory-management-270h

- https://deepak4blogger.blogspot.com/2017/09/generations-improving-performance.html
