'''online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.'''

class Payment :
    def process_payment(self):
        print("processing payment...")

class CreditCard(Payment) :
    def process_payment(self):
        print("payment proceed using CreditCard")        

class UPI(Payment) :
    def process_payment(self):
        print("payment proceed using UPI")

class NetBanking(Payment) :
    def process_payment(self) :
        print("payment proceed using NetBanking")

c = CreditCard()
u = UPI()
n = NetBanking()

c.process_payment()
u.process_payment()
n.process_payment()
