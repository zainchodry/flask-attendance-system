# 🏢 Flask Employee Attendance System

A modern, responsive **Employee Attendance System** built using **Flask**, allowing organizations to easily manage employee data and attendance records with a clean and intuitive UI.

Perfect for small to mid-size businesses, schools, or any organization that wants to streamline attendance tracking.

---

## 🚀 Features

- 👤 Add and manage employee records  
- 📅 Mark daily attendance with just a click  
- 🔍 Search attendance by employee or date  
- 📊 Generate and view attendance reports  
- 🧼 Clean Bootstrap 5 UI with custom styling  
- 📦 Modular and maintainable Flask app structure  

---

## 🛠️ Tech Stack

| Technology     | Role                         |
|----------------|------------------------------|
| **Flask**      | Python web framework         |
| **Jinja2**     | HTML templating              |
| **SQLite**     | Lightweight database         |
| **Bootstrap 5**| Responsive UI components     |
| **HTML/CSS**   | Frontend styling             |


---

## 📁 Folder Structure

EMPLOYEE-ATTENDANCE/
├── pycache/
├── instance/
├── migrations/
├── templates/
│ ├── add_employee.html
│ ├── attendance_report.html
│ ├── base.html
│ ├── delete.html
│ ├── home.html
│ ├── mark_attendance.html
│ ├── search_attendance.html
│ └── view_employees.html
├── venv/
├── .gitignore
├── app.py
├── models.py
├── requirements.txt
└── README.md


---

## 📦 Installation & Setup

### 🧰 Prerequisites

- Python 3.8 or higher
- Git installed
- `virtualenv` recommended

---

### 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/zainchodry/flask-attendance-system.git
cd flask-attendance-system

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

#Install project dependencies
pip install -r requirements.txt

#Run the Flask application
python app.py

#Then open your browser and go to:
http://127.0.0.1:5000



