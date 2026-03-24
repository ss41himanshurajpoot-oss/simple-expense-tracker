from expense_manager import add_expense, read_expenses, get_total_expenses

def main_menu():
    while True:
        print("\nSimple Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added.\n")
        elif choice == '2':
            expenses = read_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for e in expenses:
                    print(f"{e['Date']} - {e['Category']} - ${e['Amount']} - {e['Description']}")
        elif choice == '3':
            total = get_total_expenses()
            print(f"Total expenses: ${total:.2f}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main_menu()
