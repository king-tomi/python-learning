from CreditCard import CreditCard

my_customers = []
if __name__ == "__main__":
    my_customers.append(CreditCard("tomi","gtb","3465 7896 5868 3452",3000))
    my_customers.append(CreditCard("tunji","gtb","3788 3756 0978 5482",2500))
    my_customers.append(CreditCard("remi","gtb","5096 9796 9563 0375",5000))

    for val in range(17):
        my_customers[0].charge(val)
        my_customers[1].charge(2*val)
        my_customers[2].charge(3*val)


    for c in range(3):
        print("Customer:", my_customers[c].get_customer())
        print("Bank:",my_customers[c].get_bank())
        print("Account:", my_customers[c].get_account())
        print("Limit:", my_customers[c].get_limit())
        print("Balance:", my_customers[c].get_balance())
        while my_customers[c].get_balance() > int(100):
            my_customers[c].make_payment(100)
            print("New balance:", my_customers[c].get_balance())
        print()