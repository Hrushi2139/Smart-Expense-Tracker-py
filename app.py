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
            writer.writerow(["id", "date", "category", "amount", "description"])

def load_expenditure():
    rec = []
    with open(DATA_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            rec.append(row)
    return rec
