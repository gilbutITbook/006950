class Person:                           #1
    def __init__(self, name, money):    #2
        self.name = name                #3
        self.money = money
    def give_money(self, other, money): #4
        self.money -= money
        other.get_money(money)
    def get_money(self, money):
        self.money += money
    def show(self):
        print('{} : {}'.format(self.name, self.money))

if __name__=="__main__":
    g = Person('greg', 5000)          #5
    j = Person('john', 2000)
    
    g.show()
    j.show()

    g.give_money(j, 2000)             #6
    print('')
    
    g.show()
    j.show()
