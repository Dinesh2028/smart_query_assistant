import sqlite3

# Connect to a new database (creates sales.db if it doesn’t exist)
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create a sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        product TEXT,
        sale_amount REAL,
        sale_date TEXT
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO sales (customer_name, product, sale_amount, sale_date)
    VALUES (?, ?, ?, ?)
''', [
    ('John Doe', 'Laptop', 1200.50, '2024-01-15'),
    ('Jane Smith', 'Phone', 800.00, '2024-02-10'),
    ('Bob Johnson', 'Tablet', 300.75, '2024-03-05'),
    ('Alice Brown', 'Laptop', 1300.00, '2024-01-20'),
    ('Charlie Davis', 'Phone', 850.25, '2024-02-15')
])

# Save changes and close
conn.commit()
conn.close()
print("Database created successfully!")