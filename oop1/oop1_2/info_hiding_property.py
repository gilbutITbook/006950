class Account:
    def __init__(self, name, money):
        self.user = name
        self.balance = money#1
        
    @property
    def balance(self):#2
        return self._balance

    @balance.setter
    def balance(self, money):#3
        if money < 0:
            return

        self._balance = money

if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000#4

    print(my_acnt.balance)#5
    
    
