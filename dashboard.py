
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def launch_dashboard(username):
    st.title("Post Performance Dashboard")

    conn = sqlite3.connect("buzzops.db")
    df = pd.read_sql_query("""
        SELECT date, likes, comments FROM posts
        WHERE username = ?
    """, conn, params=(username,))
    conn.close()

    if df.empty:
        st.info("No post data to display.")
        return

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.strftime("%b")

    # Engagement over time
    df_monthly = df.groupby("month").sum(numeric_only=True).reindex(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        fill_value=0
    )

    st.subheader("Engagement Over Time")
    st.line_chart(df_monthly[["likes", "comments"]])

    # Posts by Reaction (mocked for simplicity)
    st.subheader("Posts by Reaction")
    reaction_counts = {
        "Like": df["likes"].sum(),
        "Comment": df["comments"].sum(),
        "Share": int((df["likes"].sum() + df["comments"].sum()) * 0.6),
        "Other": int((df["likes"].sum() + df["comments"].sum()) * 0.2),
    }
    st.bar_chart(pd.Series(reaction_counts))

    # Engagement by Type (pie chart)
    st.subheader("Engagement by Type")
    fig, ax = plt.subplots()
    ax.pie(
        [reaction_counts["Like"], reaction_counts["Share"], reaction_counts["Comment"]],
        labels=["Like", "Share", "Comment"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)
