
import sqlite3

conn = sqlite3.connect("buzzops.db")
c = conn.cursor()

# Check existing columns
c.execute("PRAGMA table_info(posts)")
columns = [row[1] for row in c.fetchall()]

# Add username column if missing
if "username" not in columns:
    print("Adding 'username' column...")
    c.execute("ALTER TABLE posts ADD COLUMN username TEXT")
else:
    print("'username' column already exists.")

conn.commit()
conn.close()
print("Done.")
