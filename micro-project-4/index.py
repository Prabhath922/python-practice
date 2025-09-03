# expence manager

import json 
import csv 
from datetime import datetime 

JSON_FILE="expences.json"
CSV_FILE="expences.csv"

def load_expences():
    try:
        with open(JSON_FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def save_expenses(expences):
    with open(JSON_FILE, "w") as f:
        json.dump(expences, f, indent=4)

    # Write CSV
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "info"])
        writer.writeheader()
        writer.writerows(expences)

def add_expences(expences):
    category = input("Enter category (food, transport, etc.): ")
    amount = float(input("Enter amount: "))
    info = input("Enter info: ")

    expence ={
        "date":datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category":category,
        "amount":amount,
        "info":info
    }
    expences.append(expence)
    save_expenses(expences)
    print("added expences")

def view_expences(expences):
     if not expences:
        print("no expences found")
        return
     for e in expences:
         print(f"{e['date']} | {e['category']} | ${e['amount']} | {e['info']}")

def main():
    expence=load_expences()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice=input("please enter the number to perform action: ")

        if choice=="1":
            add_expences(expence)
        elif choice=="2":
            view_expences(expence)
        elif choice=="3":
            break
if __name__ == "__main__":
    main()



    