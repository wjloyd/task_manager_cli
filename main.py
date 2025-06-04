import sqlite3
import datetime
from tkinter.constants import INSERT

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    created_at TEXT NOT NULL
)
""")
conn.commit()

print("Welcome to the Task Manager CLI!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice 1-3: ")

    if choice == "1":
        description = input("Enter the task description: ")
        created_at = datetime.datetime.now().isoformat()
        cursor.execute("INSERT INTO tasks (description, created_at) VALUES (?, ?)", (description, created_at))
        conn.commit()
        print("Task added successfully!.")
    elif choice == "2":
        cursor.execute("SELECT id, description, created_at FROM tasks")
        rows = cursor.fetchall()
        if not rows:
            print("No tasks found!")
        else:
            for row in rows:
                print(f"{row[0]}. {row[1]} (Created: {row[2]})")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid input. Please enter 1, 2, or 3")