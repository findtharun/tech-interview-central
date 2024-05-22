## Normalization

It is a process of analyzing the given relation schemas based on their functional dependencies and primary keys to achieve the following desirable properties:

- Minimizing Redundancy
- Minimizing the Insertion, Deletion, And Update Anomalies
- Data Integrity

Resources : https://www.youtube.com/watch?v=GFQaEYEc8_8

### 1NF

- Every row in a column should have same Datatype
- Every Table should have a Primary Key
- We should not Store Repeating group of data on a single row (Id : 1, Value : a,b,,c,d)

### 2NF

- No Partial Dependency : Each Non Key Fields (Columnns/ Atrrribute) must depend on the entire Primary key.

### 3NF

- No Transitive Dependency : Non-key attributes depend only on the primary key, not on other non-key attributes.

### Boyce Code Normal Form (3.5NF)

- A table is in BCNF if it is in 3NF and every determinant is a candidate key.

### 4NF

- A table is in 4NF if it is in BCNF and has no multi-valued dependencies ( a column cannot have multiple independent multi-valued attributes)
