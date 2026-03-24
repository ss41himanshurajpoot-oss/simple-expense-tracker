# Simple Expense Tracker

A Python-based expense management application to help users track and manage daily expenses efficiently with an easy-to-use command-line interface.

---

## Features (Functional Requirements)

- Add new expenses with date, category, amount, and description.
- View all recorded expenses.
- View expenses by category.
- Display summary statistics (total spent, average expense).
- Save all data persistently in a CSV file.

## Non-Functional Requirements

- Usable Command-Line Interface (CLI).
- Reliable input validation.
- Data integrity with simple CSV file storage.
- Modular, readable Python code with comments.
- Error handling for file operations and user inputs.

## Modules

- **main.py** — Core driver program, menu interface.
- **expense_manager.py** — Functions to add, view, summarize expenses, and handle file I/O.
- **utils.py** — Helper functions for input validation and formatting.

## File Storage

- `expenses.csv` — Stores expense records (Date, Category, Amount, Description).

---

## Diagrams and Documentation

- Flowchart or pseudocode of main functions.
- Simple CSV structure explanation:
    - expenses.csv columns: Date, Category, Amount, Description
    - Example row: `2025-11-20,Food,15.50,Lunch`
- Project report detailing objectives, functionality, design decisions, and testing.

---

## Overview

This project is a Python-based expense management application. It helps users to:
- Record daily expenses.
- Categorize and describe expenses.
- View and analyze spending patterns.

---

## Setup Instructions

1. **Clone the repository:**
    ```
    git clone https://github.com/username/expense-manager.git
    cd expense-manager
    ```

2. **Create and activate a Python virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
    *(Leave the requirements file blank or omit if using only built-in modules.)*

4. **Run the application:**
    ```
    python main.py
    ```

---

## Example Usage

```
from expense_manager import add_expense
add_expense(date="2025-11-20", category="Food", amount=15.50, description="Lunch")
```

