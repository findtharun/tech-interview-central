## Context Manager

Context managers in Python are constructs that allow for the proper setup and teardown of resources. They are most commonly used with the with statement, which ensures that resources are properly released after their use, even if an error occurs during their operation.

Context managers are used for:

1. Managing resources: such as opening and closing files, acquiring and releasing locks, or establishing and tearing down network connections.
2. Ensuring cleanup: making sure that resources are properly released even if an error occurs

Check More here : https://www.freecodecamp.org/news/context-managers-in-python/

### Implementing Context Managers
There are two primary ways to implement context managers in Python:

1. Using the special methods __enter__ and __exit__.
2. Using the contextlib module.

* ```__enter__(self)```: This method is executed when the execution flow enters the context of the with statement. It typically initializes and returns the resource to be managed.
* ```__exit__(self, exc_type, exc_value, traceback)```: This method is executed when the execution flow exits the context of the with statement. It handles cleanup tasks, such as closing a file or releasing a lock.

Example : Application Connects to DB, We need to Manage Context Such that after query is executed, DB Connection has to be closed from Application.

### Context Manager Using Special Methods (Class Based Approach)

```
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        # Return False to propagate the exception, True to suppress it
        return False

# Usage example
with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    conn.commit()

# No need to manually close the connection; it's handled by the context manager after with statement is completed
```

### Context Manager Using contextlib.contextmanager (Generator Based Approach)

```
import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    connection = sqlite3.connect(db_name)
    try:
        yield connection
    finally:
        connection.close()

# Usage example
with database_connection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    conn.commit()

# No need to manually close the connection; it's handled by the context manager
```
###  Explanation
#### Using __enter__ and __exit__ Methods
- Class Definition: Define a class DatabaseConnection with an __init__ method to initialize the database name.
- enter Method: Connect to the database and return the connection object.
- exit Method: Close the connection when exiting the with block. Handle exceptions if any occur.
-Usage: Use the with statement to manage the database connection. The connection is automatically closed when exiting the with block.

#### Using contextlib.contextmanager

- Decorator: Use the @contextmanager decorator to define a generator function database_connection.
- Setup: Connect to the database.
- Yield: Yield the connection object for use within the with block. (Syntactically, generators are almost the same as normal functions, except that you need to use yield instead of return in a generator.)
- Teardown: Close the connection in the finally block, ensuring it is always closed regardless of exceptions.
- Usage: Use the with statement to manage the database connection. The connection is automatically closed when exiting the with block.

Both approaches achieve the same goal of managing a database connection within a context, ensuring that the connection is properly closed after use. The class-based approach provides more flexibility and can be more suitable for complex scenarios, while the contextlib.contextmanager approach is more concise and may be easier to read for simple cases.