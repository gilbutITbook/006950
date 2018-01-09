class Account:
    def __init__(self, name, money):
        self.user = name
        self.__balance = money#1

    def get_balance(self):
        return self.__balance#2

    def set_balance(self, money):
        if money < 0:
            return

        self.__balance = money#3

if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.__balance = -3000#4

    print(my_acnt.get_balance())
    
