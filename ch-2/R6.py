class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        try:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        except TypeError:
            print('charge Error!!! Not number')

    def MakePayment(self, amount):
        try:
            if amount < 0:
                raise ValueError("check again ! ValueError ! amount must >= 0")
            self._balance -= amount
        except TypeError:
            print('MakePayment Error!!! Not number')
        except ValueError as ve:
            print(ve)

    def printAll(self):
        print("Initial Values")
        print("---------------")
        print("balance ={0}".format(self._balance))


if __name__ == '__main__':
    cc = CreditCard(' John Doe', '1st Bank ', '5391 0375 9387 5309 ', 1000)
    cc.printAll()

    print(cc.charge(170))
    cc.charge('Error')
    cc.printAll()
    print(cc.MakePayment(100))
    cc.printAll()
    cc.MakePayment('fsadf')
    cc.MakePayment(-100)
    cc.printAll()
