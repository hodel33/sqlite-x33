# SQLiteX33

## 📋 Overview

SQLiteX33 is a lightweight and streamlined context manager for SQLite databases in Python.<br>
It simplifies the process of running SQL queries and ensures best practices such as committing transactions and closing connections.

### 🌟 Features

- **Seamless SQLite Connection Management**: Easily manage SQLite database connections without the hassle.
- **External Execute Function**: Provides a handy external function to execute SQL commands, making it easier to integrate into other modules.
- **Foreign Key Support**: Automatically enables FOREIGN KEYS for SQLite 3 out of the box.
- **Dictionary-like Row Access**: Results are returned as Row objects, allowing access by column name (e.g., `row['name']`).
- **Query Parameterization**: Support for parameterized queries to prevent SQL injection and handle data types properly.
- **Batch Operations**: Efficiently execute the same query with multiple parameter sets using SQLite's `executemany` functionality.

<br>

## ⚙️ Installation

### 🛠️ Prerequisites

1. **🐍 Python**: SQLiteX33 is a Python context manager. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **🖋️ IDE**: For code editing, [VS Code (Visual Studio Code)](https://code.visualstudio.com/) is recommended. Enhance your Python experience by adding the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

3. **🔍 SQLite Extension (Optional)**: For easier overview and editing of SQLite databases, it's good to have an SQLite extension. [@yy0931's SQLite3 Editor for VSCode](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor) is highly recommended.

### ⬇️ Steps

To set up SQLiteX33 in your project:

1. **Download**:
   Download the `sqlite_x33.py` file from this repository.

2. **Place in Project Directory**:
   Move the `sqlite_x33.py` file to the root directory of your Python project, or where you plan on using SQLiteX33.

3. **Import and Use**:
   Follow the usage instructions below to get started with SQLiteX33.

<br>

## 🚀 Usage

### 1. Import the Python Module

To use SQLiteX33, first import the module in your Python script:

```python
import sqlite_x33 as sql
```

### 2. Using the Context Manager

Fetching Data (all)
```python
result = sql.execute("path_to_db.db", "SELECT * FROM table_name")
```

Fetching Data (specific)
```python
result = sql.execute("path_to_db.db", "SELECT * FROM table_name WHERE column1 = ?", ('value1',))
```

Accessing Results by Column Name
```python
rows = sql.execute("path_to_db.db", "SELECT column1, column2 FROM table_name")
for row in rows:
    print(f"Column1: {row['column1']}, Column2: {row['column2']}")
```

Inserting Data (single query)
```python
sql.execute("path_to_db.db", "INSERT INTO table_name (column1, column2) VALUES (?, ?)", ('value1', 'value2'))
```

Inserting Data (batch query)
```python
customers = [
    ['John Smith', 'john@example.com', '2023-05-15'],
    ['Sarah Johnson', 'sarah@example.com', '2023-05-16']
]

rows_affected = sql.execute("customers.db", "INSERT INTO customers (name, email, signup_date) VALUES (?, ?, ?)", customers)
print(f"Added {rows_affected} new customers")
```

Inserting Data (dynamic batch query)
```python
customers = [
    {"name": "John Smith", "email": "john@example.com", "signup_date": "2023-05-15"},
    {"name": "Sarah Johnson", "email": "sarah@example.com", "signup_date": "2023-05-16"}
]

# Prepare SQL statement with column names from the first dictionary
columns = ', '.join(customers[0].keys())
placeholders = ', '.join(['?'] * len(customers[0]))
sql_query = f"INSERT INTO customers ({columns}) VALUES ({placeholders})"

# Extract values in the correct order for each customer
customer_data = [list(customer.values()) for customer in customers]

rows_affected = sql.execute("customers.db", sql_query, customer_data)
print(f"Added {rows_affected} new customers")
```

Updating Data
```python
sql.execute("path_to_db.db", "UPDATE table_name SET column1 = ? WHERE column2 = ?", ('new_value', 'value2'))
```

Deleting Data
```python
sql.execute("path_to_db.db", "DELETE FROM table_name WHERE column1 = ?", ('value1',))
```

<br>

## ⚠️ Important Notes

- For single queries: The sql.execute() function returns the result of a SELECT query. If the SQL command was an INSERT/UPDATE/DELETE, it returns an empty list [].
- For batch queries: The sql.execute() function returns the number of affected rows.
- When using parameters, always use placeholders (?) in the query and provide values as a tuple or list.
- Ensure the SQLite database file path provided is correct.

<br>

## 💡 Credits

Developed by [hodel33](https://github.com/hodel33) & [dyaland](https://github.com/dyaland). Enjoy and have fun! 💫

<br>

## 💬 Feedback & Contact

I'd love to network, discuss tech, or swap music recommendations. Feel free to connect with me on:

🌐 **LinkedIn**: [Björn Hödel](https://www.linkedin.com/in/bjornhodel)<br>
🐦 **Twitter**: [@hodel33](https://twitter.com/hodel33)<br>
📸 **Instagram**: [@hodel33](https://www.instagram.com/hodel33)<br>
📧 **Email**: [hodel33@gmail.com](mailto:hodel33@gmail.com)
