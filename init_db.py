import sqlite3
from sqlite3 import Error

# Database initialization function
def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Connection to database {db_file} successful.')
    except Error as e:
        print(e)
    return conn

# Create a table for managing books

def create_books_table(conn):
    """
    Create a table for books
    """
    try:
        sql_create_books_table = '''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT NOT NULL,
            publication_year INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
        cursor = conn.cursor()
        cursor.execute(sql_create_books_table)
    except Error as e:
        print(e)

# Main function
if __name__ == '__main__':
    database = "books.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create books table
    if conn:
        create_books_table(conn)
        conn.close()