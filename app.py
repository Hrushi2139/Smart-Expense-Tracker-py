import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE ="expenditure.csv"

def storage_setup():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "expenditure_date", "expense_type", "amount", "desc"])

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
        datetime.strptime(expenditure_date, "%Y-%m-%d")

        expense_type = input("Enter expense_type: ")
        amount = float(input("Enter amount: "))
        desc = input("Enter desc: ")

        data = load_expenditure()
        new_id = len(data) + 1

        with open(DATA_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([new_id, expenditure_date, expense_type, amount, desc])

        print("New Expense Added")

    except:
        print("Invalid Input")

def show_expenses():
    rec = load_expenditure()

    if not rec:
        print("No expenses found")
        return

    for e in rec:
        print(f"{e['id']} | {e['expenditure_date']} | {e['expense_type']} | ₹{e['amount']} | {e['desc']}")


def delete_expense():
    rec = load_expenditure()
    show_expenses()

    try:
        id_del = input("Enter ID to delete: ")

        new_data = [d for d in rec if d["id"] != id_del]

        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "expenditure_date", "expense_type", "amount", "desc"])

            for i, d in enumerate(new_data, start=1):
                writer.writerow([i, d["expenditure_date"], d["expense_type"], d["amount"], d["desc"]])

        print("Expense deleted Successfully")

    except:
        print("Error")

def search_expense():
    search_term = input("Enter keyword: ").lower()
    rec = load_expenditure()

    found = False
    for e in rec:
        if search_term in e["expense_type"].lower() or search_term in e["desc"].lower():
            print(f"{e['expenditure_date']} | {e['expense_type']} | ₹{e['amount']} | {e['desc']}")
            found = True

    if not found:
        print("No matching results")
