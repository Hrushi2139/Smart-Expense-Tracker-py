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

        rec = load_expenditure()
        new_id = len(rec) + 1

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


def monthly_report():
    rec = load_expenditure()
    month = input("Enter month (YYYY-MM): ")

    total = 0
    expense_type_data = defaultdict(float)

    for e in rec:
        if e["expenditure_date"].startswith(month):
            total += e["amount"]
            expense_type_data[e["expense_type"]] += e["amount"]

    if total == 0:
        print("No data found")
        return None

    print(f"Total: ₹{total}")
    for c, a in expense_type_data.items():
        print(f"{c}: ₹{a}")

    return expense_type_data, month


def show_chart(expense_type_data, title_name):
    if not expense_type_data:
        return

    chart_labels = list(expense_type_data.keys())
    chart_values = list(expense_type_data.values())

    plt.pie(chart_values, labels=chart_labels, autopct="%1.1f%%")
    plt.title(title_name)
    plt.show()


def total_summary():
    rec = load_expenditure()

    total = 0
    expense_type_data = defaultdict(float)

    for e in rec:
        total += e["amount"]
        expense_type_data[e["expense_type"]] += e["amount"]

    print(f"\nTotal: ₹{total}")
    for c, a in expense_type_data.items():
        print(f"{c}: ₹{a}")

    return expense_type_data


def generate_insights():
    rec = load_expenditure()

    if not rec:
        print("No data available")
        return

    total = sum(e["amount"] for e in rec)
    avg_amount= total / len(rec)

    highest = max(rec, key=lambda x: x["amount"])
    lowest = min(rec, key=lambda x: x["amount"])

    print("\n*******************INSIGHTS****************")
    print(f"Total Spending: ₹{total}")
    print(f"Average Expense: ₹{avg_amount:.2f}")
    print(f"Highest Expense: ₹{highest['amount']} ({highest['expense_type']})")
    print(f"Lowest Expense: ₹{lowest['amount']} ({lowest['expense_type']})")
    

def main():
    storage_setup()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Monthly Summary")
        print("6. Overall Summary")
        print("7. Insights")
        print("8. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_expense()
        elif ch == "2":
            show_expenses()
        elif ch == "3":
            delete_expense()
        elif ch == "4":
            search_expense()
        elif ch == "5":
            res = monthly_report()
            if res:
                data, m = res
                show_chart(data, f"Monthly ({m})")
        elif ch == "6":
            data = total_summary()
            show_chart(data, "Overall")
        elif ch == "7":
            generate_insights()
        elif ch == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()