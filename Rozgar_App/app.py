import streamlit as st
import json
import os

# --- Data Manager Class ---
class DataManager:
    def __init__(self, file_path='data/workers.json'):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def add_worker(self, worker):
        data = self.get_all_workers()
        data.append(worker)
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all_workers(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def delete_worker(self, name, contact):
        data = self.get_all_workers()
        data = [worker for worker in data if not (worker.get("name") == name and worker.get("contact") == contact)]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return "Worker deleted successfully!"

# Initialize Data Manager
data_manager = DataManager()

# --- Login Page ---
def login():
    st.title("RozgarLink – Local Job Finder")
    st.subheader("🔐 Login to Continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if username and password:
            st.session_state.user = username
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error("Please enter both username and password.")

# --- Main App Function ---
def main_app():
    st.sidebar.title("🏢 Rozgar Menu")
    menu = st.sidebar.radio("Select an Option", ["Register", "Search Workers", "Delete Account"])

    if menu == "Register":
        st.subheader("👤 Register as a Worker")
        name = st.text_input("Your Name")
        skill = st.text_input("Skill")
        city = st.text_input("City")
        contact = st.text_input("Contact Number")

        if st.button("Register"):
            if name and skill and city and contact:
                worker = {"name": name, "skill": skill, "city": city, "contact": contact}
                data_manager.add_worker(worker)
                st.success(f"Worker {name} registered successfully!")
            else:
                st.error("Please fill all the details")

    elif menu == "Search Workers":
        st.subheader("🔍 Search for Workers")
        city = st.text_input("Enter City")
        skill = st.text_input("Enter Skill")
        results = data_manager.get_all_workers()

        if city:
            results = [w for w in results if w.get("city", "").lower() == city.lower()]
        if skill:
            results = [w for w in results if w.get("skill", "").lower() == skill.lower()]

        if results:
            for worker in results:
                st.write(f"{worker.get('name', 'N/A')} | {worker.get('skill', 'N/A')} | {worker.get('city', 'N/A')} | {worker.get('contact', 'N/A')}")
        else:
            st.warning("No workers found.")

    elif menu == "Delete Account":
        st.subheader("🚮 Delete Your Registration")
        name = st.text_input("Enter Your Name")
        contact = st.text_input("Enter Your Contact Number")

        if st.button("Delete Account"):
            if name and contact:
                result = data_manager.delete_worker(name, contact)
                st.success(result)
            else:
                st.error("Please enter name and contact to delete account")

# --- App Execution ---
if 'user' not in st.session_state:
    login()
else:
    main_app()
