import sqlite3

# Open a connection to the database file
conn = sqlite3.connect('passwords_examples.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the passwords
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT
    )
''')

# Open the text file
# Here is where you input any file that has a list of common passwords if needed instead of inputing every input
with open('password.txt') as f:
    # Read the lines from the file
    lines = f.readlines()

    # Insert each line into the table
    for line in lines:
        cursor.execute('''
            INSERT INTO passwords (password)
            VALUES (?)
        ''', (line.strip(),))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()