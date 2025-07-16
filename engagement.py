
import streamlit as st
import sqlite3
import base64
from datetime import datetime

def show_archive(username):
    st.title("Post Archive")

    # Month & Year filter
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    selected_month = st.selectbox("Select Month", months)
    selected_year = st.selectbox("Year", [2025])

    month_index = months.index(selected_month) + 1

    conn = sqlite3.connect("buzzops.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            content TEXT,
            date TEXT,
            likes INTEGER DEFAULT 0,
            comments INTEGER DEFAULT 0,
            image TEXT
        )
    """)

    c.execute("""
        SELECT content, date, likes, comments, image FROM posts
        WHERE username = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        ORDER BY date DESC
    """, (username, f"{month_index:02}", str(selected_year)))

    posts = c.fetchall()
    conn.close()

    if not posts:
        st.info("No posts found for this month.")
    else:
        for post in posts:
            content, date, likes, comments, image = post
            st.write("###", content)
            if image:
                st.image(base64.b64decode(image), use_container_width=True)
            st.write(f"**{likes} Likes** | **{comments} Comments** — {date}")
            st.markdown("---")
