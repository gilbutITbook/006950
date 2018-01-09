class Account:
    def __init__(self, name, money):
        self.user = name
        self.balance = money

    def get_balance(self):
        return self.balance

    def set_balance(self, money):
        if money < 0:
            return

        self.balance = money

if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000   #1

    print(my_acnt.get_balance())
