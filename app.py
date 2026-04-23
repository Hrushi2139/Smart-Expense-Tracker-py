import csv
import os
from expenditure_datetime import expenditure_datetime
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE ="expenditure.csv"

def storage_setup():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writeentry(["id", "expenditure_date", "expense_type", "amount", "description"])

def load_expenditure():
    rec = []
    with open(DATA_FILE, "r") as f:
        reader = csv.DictReader(f)
        for entry in reader:
            entry["amount"] = float(entry["amount"])
            rec.append(entry)
    return rec

def add_expense():
    try:
        expenditure_date = input("Enter expenditure_date (YYYY-MM-DD): ")
        expenditure_datetime.strptime(expenditure_date, "%Y-%m-%d")

        expense_type = input("Enter expense_type: ")
        amount = float(input("Enter amount: "))
        desc = input("Enter description: ")

        data = read_data()
        new_id = len(data) + 1

        with open(DATA_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writeentry([new_id, expenditure_date, expense_type, amount, desc])

        print("New Expense Added")

    except:
        print("Invalid Input")