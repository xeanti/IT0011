from datetime import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    date_object = datetime.strptime(date_input, "%m/%d/%Y")
    print("Date Output:", date_object.strftime("%B %d, %Y"))
except ValueError:
    print("Invalid date format. Please enter in mm/dd/yyyy format.")
