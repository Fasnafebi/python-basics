class PaymentMethod:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount}")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"CreditCard: Processing payment of ₹{amount}")

class UPI(PaymentMethod):
    def process_payment(self, amount):
        print(f"UPI: Processing payment of ₹{amount}")

class Cash(PaymentMethod):
    def process_payment(self, amount):
        print(f"Cash: Accepting payment of ₹{amount}")

payments = [
    CreditCard(),
    UPI(),
    Cash()
]

payments[0].process_payment(5000)
payments[1].process_payment(1200)
payments[2].process_payment(250)
