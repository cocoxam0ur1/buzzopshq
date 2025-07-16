
import sqlite3

conn = sqlite3.connect("buzzops.db")
c = conn.cursor()

# Check existing columns
c.execute("PRAGMA table_info(posts)")
columns = [row[1] for row in c.fetchall()]

# Add content column if missing
if "content" not in columns:
    print("Adding 'content' column...")
    c.execute("ALTER TABLE posts ADD COLUMN content TEXT")
else:
    print("'content' column already exists.")

conn.commit()
conn.close()
print("Done.")
