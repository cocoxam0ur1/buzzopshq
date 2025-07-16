
import streamlit as st
import sqlite3
from datetime import datetime
import base64

def schedule_post(username):
    st.title("Calendar Scheduler")
    post_content = st.text_input("Enter post content")
    image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    date = st.date_input("Select post date", min_value=datetime.now().date())

    if st.button("Schedule Post"):
        if post_content:
            image_data = None
            if image_file:
                image_data = base64.b64encode(image_file.read()).decode("utf-8")

            conn = sqlite3.connect("buzzops.db")
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    content TEXT,
                    caption TEXT NOT NULL DEFAULT '',
                    date TEXT,
                    likes INTEGER DEFAULT 0,
                    comments INTEGER DEFAULT 0,
                    image TEXT
                )
            """)
            c.execute("""
                INSERT INTO posts (username, content, caption, date, image)
                VALUES (?, ?, ?, ?, ?)
            """, (username, post_content, post_content, date.isoformat(), image_data))
            conn.commit()
            conn.close()
            st.success("Post scheduled successfully!")
        else:
            st.error("Please enter post content before scheduling.")
