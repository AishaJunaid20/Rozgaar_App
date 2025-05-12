# RozgarLink – Local Job Finder for Skilled Workers 🇵🇰

RozgarLink is a simple, interactive web application built using **Python** and **Streamlit**, designed to connect skilled workers in Pakistan with job opportunities near them. It offers a clean and user-friendly interface where individuals can **register their skills**, **search for other workers**, and **delete their profiles** if needed.


## 🧠 Problem Solved

In Pakistan, many skilled workers (like electricians, plumbers, tailors, etc.) do not have easy access to platforms to showcase their services or find local jobs. RozgarLink bridges that gap by allowing workers to register and be discoverable by location and skill — no complex signups or mobile apps required.


## 🚀 Features

- 📝 **Register** your name, skill, city, and contact number.
- 🔍 **Search** other registered workers by skill and city.
- ❌ **Delete** your registration if you no longer want to appear in the directory.
- 🔐 **Simple Login** to prevent spam entries (anyone can log in for now).
- 📂 Data is stored in a local JSON file using **Object-Oriented Programming (OOP)** concepts.
- 📱 **Responsive** and runs instantly in any browser using Streamlit


## ⚙️ Technologies Used

- **Python**
- **Streamlit** for building the web interface
- **JSON** for storing user data
- **Object-Oriented Programming (OOP)** for managing data logic



## 🧰 Where OOP is Used

The app uses a class called `DataManager` to handle:
- Adding new worker registrations
- Reading all existing registrations
- Deleting workers by name and contact

This encapsulation of logic ensures code **reusability**, **clean structure**, and **separation of concerns** — a key benefit of OOP.


## 📸 How It Works

1. User logs in.
2. Registers their skills, city, and contact info.
3. Searches for others or deletes their own record if needed.
4. Data is saved in `data/workers.json`.


🤝 Author
Made by Aisha Junaid to empower skilled workers across Pakistan 🌟
Proudly built with ❤️ and Python.



