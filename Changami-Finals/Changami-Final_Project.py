import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        middle_name TEXT,
                        last_name TEXT NOT NULL,
                        birthday TEXT NOT NULL,
                        gender TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_user(first_name, middle_name, last_name, birthday, gender):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (first_name, middle_name, last_name, birthday, gender) VALUES (?, ?, ?, ?, ?)",
                       (first_name, middle_name, last_name, birthday, gender))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Database error: {e}")

def fetch_all():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    conn.close()
    return records

def search_record(last_name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE last_name = ?", (last_name,))
    record = cursor.fetchall()
    conn.close()
    return record

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management System")
        self.root.geometry("400x300")
        self.root.configure(bg="#ffffff")
        
        self.menu_frame = tk.Frame(root, bg="#4a90e2")
        self.menu_frame.pack(fill="both", expand=True)
        
        tk.Label(self.menu_frame, text="User Management System", font=("Arial", 16), bg="#4a90e2", fg="#ffffff").pack(pady=10)
        tk.Button(self.menu_frame, text="Sign-up", command=self.signup_window, bg="#5cb85c", fg="#ffffff", font=("Arial", 12)).pack(pady=5, padx=10, fill='x')
        tk.Button(self.menu_frame, text="View all records", command=self.view_records, bg="#5bc0de", fg="#ffffff", font=("Arial", 12)).pack(pady=5, padx=10, fill='x')
        tk.Button(self.menu_frame, text="Search a record", command=self.search_window, bg="#f0ad4e", fg="#ffffff", font=("Arial", 12)).pack(pady=5, padx=10, fill='x')
        tk.Button(self.menu_frame, text="Exit", command=root.quit, bg="#d9534f", fg="#ffffff", font=("Arial", 12)).pack(pady=5, padx=10, fill='x')

    def signup_window(self):
        signup = tk.Toplevel(self.root)
        signup.title("Sign-up Form")
        signup.geometry("350x250")
        signup.configure(bg="#ecf0f1")
        
        form_frame = tk.Frame(signup, bg="#ecf0f1")
        form_frame.pack(pady=30)

        tk.Label(form_frame, text="First Name", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Middle Name", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Last Name", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Birthday (YYYY-MM-DD)", bg="#ecf0f1").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Gender", bg="#ecf0f1").grid(row=4, column=0, padx=10, pady=5)
        
        first_name = tk.Entry(form_frame)
        middle_name = tk.Entry(form_frame)
        last_name = tk.Entry(form_frame)
        birthday = tk.Entry(form_frame)
        gender = ttk.Combobox(form_frame, values=["Male", "Female", "Other"])
        
        first_name.grid(row=0, column=1, padx=10, pady=5)
        middle_name.grid(row=1, column=1, padx=10, pady=5)
        last_name.grid(row=2, column=1, padx=10, pady=5)
        birthday.grid(row=3, column=1, padx=10, pady=5)
        gender.grid(row=4, column=1, padx=10, pady=5)
        
        def submit():
            if not first_name.get() or not last_name.get() or not birthday.get() or not gender.get():
                messagebox.showerror("Error", "Please fill all required fields.")
                return
            insert_user(first_name.get(), middle_name.get(), last_name.get(), birthday.get(), gender.get())
            signup.destroy()
        
        tk.Button(form_frame, text="Submit", command=submit, bg="#5cb85c", fg="#ffffff").grid(row=5, columnspan=2, pady=10)

    def view_records(self):
        records_window = tk.Toplevel(self.root)
        records_window.title("All Records")
        records_window.geometry("600x300")

        tree = ttk.Treeview(records_window, columns=("ID", "First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Birthday", text="Birthday")
        tree.heading("Gender", text="Gender")

        tree.column("ID", width=30)
        tree.column("First Name", width=100)
        tree.column("Middle Name", width=100)
        tree.column("Last Name", width=100)
        tree.column("Birthday", width=100)
        tree.column("Gender", width=80)

        records = fetch_all()
        for record in records:
            tree.insert("", tk.END, values=record)

        tree.pack(expand=True, fill='both')

    def search_window(self):
        search = tk.Toplevel(self.root)
        search.title("Search Record")
        search.geometry("350x150")
        search.configure(bg="#ecf0f1")
        
        tk.Label(search, text="Enter Last Name", bg="#ecf0f1").pack(pady=5)
        last_name_entry = tk.Entry(search)
        last_name_entry.pack(pady=5)
        
        def search_result():
            last_name = last_name_entry.get()
            records = search_record(last_name)
            result_window = tk.Toplevel(search)
            result_window.title("Search Result")
            text = tk.Text(result_window)
            text.pack(expand=True, fill='both')
            if records:
                for record in records:
                    text.insert(tk.END, f"{record}\n")
            else:
                text.insert(tk.END, "No record found.")
        
        tk.Button(search, text="Search", command=search_result, bg="#5bc0de", fg="#ffffff").pack(pady=10)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()