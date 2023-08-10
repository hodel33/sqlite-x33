# SQLiteX33

## Introduction

SQLiteX33 is a lightweight and streamlined context manager for SQLite databases.<br>
It simplifies the process of running SQL queries and ensures best practices such as committing transactions and closing connections.

## Features

- **Seamless SQLite Connection Management**: Easily manage SQLite database connections without the hassle.
- **External Execute Function**: Provides a handy external function to execute SQL commands, making it easier to integrate into other modules.
- **Foreign Key Support**: Automatically enables FOREIGN KEYS for SQLite 3 out of the box.
  
## Usage

### 1. Import the module

```python
import sqlite_x33 as sql
```

### 2. Using the Context Manager

Fetching Data
```python
result = sql.execute("path_to_db.db", "SELECT * FROM table_name")
```

Inserting Data
```python
sql.execute("path_to_db.db", "INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2')")
```

Updating Data
```python
sql.execute("path_to_db.db", "UPDATE table_name SET column1 = 'new_value' WHERE column2 = 'value2'")
```

Deleting Data
```python
sql.execute("path_to_db.db", "DELETE FROM table_name WHERE column1 = 'value1'")
```

## Important Notes

- The sql.execute() function returns the result of a SELECT query. If the SQL command was an INSERT/UPDATE/DELETE, it returns None.
- Ensure the SQLite database file path provided is correct.

## Credits

Developed by [hodel33](https://github.com/hodel33) & [dyaland](https://github.com/dyaland). Enjoy and have fun! 🚀
