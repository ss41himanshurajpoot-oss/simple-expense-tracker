import csv

FILENAME = "expenses.csv"
FIELDNAMES = ['Date', 'Category', 'Amount', 'Description']

def add_expense(date, category, amount, description):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        # Write header only if file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'Date': date,
            'Category': category,
            'Amount': amount,
            'Description': description
        })

def read_expenses():
    expenses = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass  # No file yet
    return expenses

def get_total_expenses():
    expenses = read_expenses()
    total = 0.0
    for e in expenses:
        total += float(e['Amount'])
    return total
