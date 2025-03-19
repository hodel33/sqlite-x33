import sqlite3 as sql

class SQLiteX33:
    """A streamlined SQLite Database Context Manager for easy SQL queries. Import as 'import sqlite_x33 as sql', then use sql.execute(db, query). /hodel33 & dyaland"""
    def __init__(self, db_file_path:str):
        self.db_file = db_file_path
        
    def __enter__(self):
        self.connection = sql.connect(self.db_file)
        self.connection.row_factory = sql.Row  # Enable dictionary-like row access, e.g. row['name']
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = True;") # enabling FOREIGN KEYS for SQLite 3
        return self
    
    def __exit__(self, exc_class, exc, traceback):
        try:
            self.connection.commit()
        except AttributeError: # isn't closable
            return True # exception handled successfully
        finally:
            self.cursor.close(); self.connection.close()
     
    def execute_query(self, query:str, params=()):
        if isinstance(params, list) and len(params) > 0 and isinstance(params[0], (list, tuple)): # Batch operation
            self.cursor.executemany(query, params)
            return self.cursor.rowcount  # Return number of affected rows for batch INSERT/UPDATE/DELETE
        else: # Single operation
            self.cursor.execute(query, params)
            return self.cursor.fetchall()  # Returns the result of a SELECT query; None if the query was INSERT/UPDATE/DELETE

def execute(db_path:str, query:str, params=()):
    with SQLiteX33(db_path) as db:
        return db.execute_query(query, params)
