transactions = [
    {"id": 1, "amount": 250, "type": "credit"},
    {"id": 2, "amount": 100, "type": "debit"},
    {"id": 3, "amount": 50, "type": "debit"},
    {"id": 4, "amount": 400, "type": "credit"},
]

def calculate_balance(transactions):
    balance = 0
    for txn in transactions:
        if txn["type"] == "credit":
            balance += txn["amount"]
        elif txn["type"] == "debit":
            balance -= txn["amount"]
    return balance

final_balance = calculate_balance(transactions)
print("Final Balance:", final_balance)