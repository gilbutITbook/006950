#계좌 클래스 구현
class Account:
    num_acnt = 0     #1

    @classmethod
    def get_num_acnt(cls):    #2
        '''
        cls.get_num_acnt() -> integer
        '''
        return cls.num_acnt
    
    def __init__(self, name, money):
        self.user = name         #3
        self.balance = money
        Account.num_acnt += 1    #4

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):
        '''
        obj.transfer(other, money) -> bool
        other : The object to interact with
        money : money the user wants to send

        returns True if the balance is enough to transfer
        returns False if not
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)
            
if __name__== "__main__":
    #객체 생성
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    #생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print()

    #인스턴스 메서드를 호출하는 방법
    #1. by object
    my_acnt.deposit(500)              #5
    #2. by class
    #Account.deposit(my_acnt, 500)    #6

    #deposit 확인
    print('deposit')
    print(my_acnt)
    print()
    
    #withdraw 함수 사용법
    print('withdraw')
    money = my_acnt.withdraw(1500)
    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print()
    
    #클래스 멤버에 접근하는 방법
    print('class member')
    #1.by class 
    print(Account.num_acnt)    
    #2.by object
    #print(my_acnt.num_acnt)
    print()

    #클래스 메서드를 호출하는 방법
    print('class method')
    #1.by class
    n_acnt = Account.get_num_acnt()
    #2.by object
    #n_acnt = my_acnt.get_num_acnt()
    
    print('The number of accounts : {}'.format(n_acnt))
    print()
    
    #메시지 패싱 
    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)
    
