- A foreign key must reference a unique key in another table.

  - The referenced key can be a primary key or any unique key.
  - The purpose of a foreign key is to maintain referential integrity between two tables.

- Order of appearance of the common statements in the SELECT query

  - `SELECT – FROM – JOIN – ON – WHERE – GROUP BY – HAVING – ORDER BY – LIMIT`

- Order in which interpreter executes the common statements in the SELECT query

  - `FROM – JOIN – ON – WHERE – GROUP BY – HAVING – SELECT – ORDER BY – LIMIT`

- DELETE statement is <b> Reversibele </b> - (ROLLBACK) is possible. Delete Statement is Slower Compared to TRUNCATE

- TRUNCATE statement is <b> Irreversibele </b> - (ROLLBACK) is not possible. It is quicker.

### ACID Properties

- Atomicity : Commit all or Nothing (either the entire transaction takes place at once or doesn’t happen at all)

- Consistency : Integrity constraints must be maintained so that the database is consistent before and after the transaction.
  (Eg : for a Transaction in account (If we have the Minimum Balance as Constraint), then it should be maintained throught or should revert back transaction if it is voilated.)

- Isolation : Multiple transactions can occur concurrently without leading to the inconsistency of the database state.

- Durabaility : Data is Persisted after transation is commited even in a system failure.

Explanation : https://www.youtube.com/watch?v=GAe5oB742dw