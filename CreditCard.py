class CreditCard:
    """A program that models a credit card for a particular customer.
       Parameters:

        customer: the name of the customer

        bank: the name of the bank

        account: the kind of account.

        limit: the limit of transaction.

            balance: this is set to zero at initialization"""

    def __init__(self,customer,bank,account,limit):

        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.account

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def charge(self,price):
        """this method charges the customer by adding the balance to the price included"""
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self,amount):
        """This makes payment based on the amount input."""
        try:
          if amount > 0:
            self.balance -= amount
          elif amount == 0:
            self.balance += 0
        except ValueError:
            print("can't have negative value")