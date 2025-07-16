
import streamlit as st
from login import verify_login, register_user, init_db
from dashboard import launch_dashboard
from scheduler import schedule_post
from engagement import show_archive

def main():
    st.set_page_config(page_title="BuzzOps HQ", layout="wide")
    st.sidebar.title("BuzzOps HQ")
    page = st.sidebar.radio("Navigate", ["Dashboard", "Archive", "Calendar"])

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    init_db()

    if not st.session_state.logged_in:
        tabs = st.tabs(["Login", "Register"])

        with tabs[0]:
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Login")
                if submitted:
                    if verify_login(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success("Login successful!")
                    else:
                        st.error("Invalid username or password")

        with tabs[1]:
            with st.form("register_form"):
                new_user = st.text_input("New Username")
                new_pass = st.text_input("New Password", type="password")
                reg_submit = st.form_submit_button("Register")
                if reg_submit:
                    if register_user(new_user, new_pass):
                        st.success("Registration successful! Please log in.")
                    else:
                        st.error("Username already exists.")
        return

    st.sidebar.success(f"Welcome, {st.session_state.username}!")

    if page == "Dashboard":
        launch_dashboard(st.session_state.username)
    elif page == "Archive":
        show_archive(st.session_state.username)
    elif page == "Calendar":
        schedule_post(st.session_state.username)

if __name__ == "__main__":
    main()
