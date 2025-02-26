import streamlit as st

# Fake Users Database (Replace with a real database in production)
users_db = {
    "user@example.com": {"name": "John Doe", "password": "1234"}
}

def signin_page():
    st.subheader("Sign In")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in users_db and users_db[email]["password"] == password:
            st.success(f"Welcome back, {users_db[email]['name']}! ✅")
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()
        else:
            st.error("Invalid Email or Password!")

def signup_page():
    st.subheader("Sign Up")
    
    new_email = st.text_input("Enter Email")
    new_name = st.text_input("Enter Full Name")
    new_password = st.text_input("Enter Password", type="password")

    if st.button("Register"):
        if new_email in users_db:
            st.error("Email already registered! Try signing in.")
        else:
            users_db[new_email] = {"name": new_name, "password": new_password}
            st.success("Account created successfully! ✅ You can now Sign In.")
