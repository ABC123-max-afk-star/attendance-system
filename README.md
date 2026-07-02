Project Overview

The Attendance Management System is a simple Python-based application designed to manage student attendance efficiently. It helps automate the process of adding students, marking attendance, and generating records using a database system.

🚀 Features
➕ Add new students with details (Name, Roll Number, Department)
🔍 Search student by name or roll number
✏️ Update student information
❌ Delete student records
📅 Mark daily attendance (Present/Absent)
📊 View attendance records
🛠️ Technologies Used
Python 🐍
Tkinter (for GUI) or Flask (if web-based)
MySQL / SQLite (Database)
SQL for data management
📁 Project Structure
attendance_system/
│
├── app.py            # Main application file
├── database.py       # Database connection file
├── check_db.py       # Table creation script (optional)
├── README.md         # Project documentation
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/attendance-system.git
2. Move to project folder
cd attendance-system
3. Install required libraries
pip install mysql-connector-python
4. Set up database
Create database in MySQL:
CREATE DATABASE attendance_db;
Run table creation queries provided in the project
5. Run the application
python app.py
🧑‍💻 How It Works
Run the application
Add student details into the system
Mark attendance daily (Present/Absent)
View or search student records anytime
Data is stored securely in MySQL database
📊 Future Improvements
Cloud database integration
Login authentication system
Attendance reports (PDF/Excel export)
Face recognition attendance system
👨‍🎓 Author
Name: mohammad ikhlas
College: SRM University AP
Project: Academic Mini Project
📜 License

This project is for educational purposes only.
