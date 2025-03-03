import json
import os

class StudentRecordManager:
    def __init__(self):
        self.records = []
        self.filename = None

    def load_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.records = json.load(file)
            self.filename = filename
            print(f"Loaded {len(self.records)} records from {filename}")
        else:
            print("File not found.")

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.records, file, indent=4)
            print(f"Records saved to {self.filename}")
        else:
            print("No file opened. Use 'Save As' instead.")

    def save_as_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.records, file, indent=4)
        self.filename = filename
        print(f"Records saved as {filename}")

    def show_all_records(self):
        for record in self.records:
            print(record)

    def order_by_lastname(self):
        self.records.sort(key=lambda x: x[1][1])
        self.show_all_records()

    def order_by_grade(self):
        self.records.sort(key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
        self.show_all_records()

    def show_student_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Student not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added.")

    def edit_record(self, student_id, new_class_standing=None, new_major_exam=None):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                new_record = list(record)
                if new_class_standing is not None:
                    new_record[2] = new_class_standing
                if new_major_exam is not None:
                    new_record[3] = new_major_exam
                self.records[i] = tuple(new_record)
                print("Record updated.")
                return
        print("Student not found.")

    def delete_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                self.records.remove(record)
                print("Record deleted.")
                return
        print("Student not found.")

def main():
    manager = StudentRecordManager()
    while True:
        print("""
        1. Open File
        2. Save File
        3. Save As File
        4. Show All Students Record
        5. Order by Last Name
        6. Order by Grade
        7. Show Student Record
        8. Add Record
        9. Edit Record
        10. Delete Record
        11. Exit
        """)
        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter filename: ")
            manager.load_file(filename)
        elif choice == "2":
            manager.save_file()
        elif choice == "3":
            filename = input("Enter new filename: ")
            manager.save_as_file(filename)
        elif choice == "4":
            manager.show_all_records()
        elif choice == "5":
            manager.order_by_lastname()
        elif choice == "6":
            manager.order_by_grade()
        elif choice == "7":
            student_id = input("Enter student ID: ")
            manager.show_student_record(student_id)
        elif choice == "8":
            student_id = input("Enter Student ID (6 digits): ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "9":
            student_id = input("Enter Student ID: ")
            class_standing = input("Enter new Class Standing Grade (leave blank to skip): ")
            major_exam = input("Enter new Major Exam Grade (leave blank to skip): ")
            manager.edit_record(student_id, float(class_standing) if class_standing else None, float(major_exam) if major_exam else None)
        elif choice == "10":
            student_id = input("Enter Student ID: ")
            manager.delete_record(student_id)
        elif choice == "11":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
