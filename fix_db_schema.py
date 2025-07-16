
import sqlite3

# Connect to the existing buzzops.db file
conn = sqlite3.connect("buzzops.db")
c = conn.cursor()

# Get current column names
c.execute("PRAGMA table_info(posts)")
existing_columns = [row[1] for row in c.fetchall()]

# Define expected columns
required_columns = {
    "date": "TEXT",
    "likes": "INTEGER DEFAULT 0",
    "comments": "INTEGER DEFAULT 0",
    "image": "TEXT"
}

# Add missing columns
for column, col_type in required_columns.items():
    if column not in existing_columns:
        print(f"Adding column: {column}")
        c.execute(f"ALTER TABLE posts ADD COLUMN {column} {col_type}")

conn.commit()
conn.close()
print("Schema fix complete. You can now run the app.")
