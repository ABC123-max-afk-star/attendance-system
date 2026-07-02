from tkinter import *
from tkinter import messagebox
import sqlite3

DB_NAME = "my_new_db.db"

# ---------- Database Setup ----------
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    status TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

# ---------- Main Window ----------
root = Tk()
root.title("Student Attendance System")
root.geometry("500x700")


# ---------- Functions ----------
def load_students():
    student_list.delete(0, END)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, roll FROM students")
    rows = cursor.fetchall()

    for row in rows:
        student_list.insert(END, f"{row[0]} - {row[1]}")

    conn.close()


def add_student():
    name = name_entry.get()
    roll = roll_entry.get()

    if name == "" or roll == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, roll) VALUES (?, ?)",
        (name, roll)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Added Successfully")

    name_entry.delete(0, END)
    roll_entry.delete(0, END)

    load_students()


def search_student():
    keyword = search_entry.get()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, roll FROM students WHERE name LIKE ? OR roll LIKE ?",
        ('%' + keyword + '%', '%' + keyword + '%')
    )

    rows = cursor.fetchall()

    student_list.delete(0, END)

    for row in rows:
        student_list.insert(END, f"{row[0]} - {row[1]}")

    conn.close()


def mark_present():
    selected = student_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first")
        return

    student = student_list.get(selected[0])

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (student, status, date) VALUES (?, ?, date('now'))",
        (student, "Present")
    )

    conn.commit()
    conn.close()

    attendance_list.insert(END, f"{student} - Present")


def mark_absent():
    selected = student_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first")
        return

    student = student_list.get(selected[0])

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (student, status, date) VALUES (?, ?, date('now'))",
        (student, "Absent")
    )

    conn.commit()
    conn.close()

    attendance_list.insert(END, f"{student} - Absent")


# ---------- UI ----------
title = Label(root, text="Student Attendance System", font=("Arial", 20))
title.pack(pady=10)

Label(root, text="Student Name").pack()
name_entry = Entry(root, width=30)
name_entry.pack()

Label(root, text="Roll Number").pack()
roll_entry = Entry(root, width=30)
roll_entry.pack()

Button(root, text="Add Student", command=add_student).pack(pady=10)

Label(root, text="Search Student").pack()
search_entry = Entry(root, width=30)
search_entry.pack()

Button(root, text="Search", command=search_student).pack(pady=5)
Button(root, text="Show All Students", command=load_students).pack(pady=5)

student_list = Listbox(
    root,
    width=40,
    height=8,
    selectmode=SINGLE,
    exportselection=False
)
student_list.pack(pady=10)

Button(root, text="Present", command=mark_present).pack()
Button(root, text="Absent", command=mark_absent).pack(pady=5)

Label(root, text="Attendance Report").pack()

attendance_list = Listbox(root, width=50, height=10)
attendance_list.pack(pady=10)

load_students()

root.mainloop()