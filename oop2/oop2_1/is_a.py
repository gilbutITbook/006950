#IS-A
class Computer:
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram
        
    def browse(self):
        print('browse')

    def work(self):
        print('work')

class Laptop(Computer):                       #1
    #멤버 추가
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu, ram)            #2
        self.battery = battery                #3
    #메서드 추가
    def move(self, to):                       #4
        print('move to {}'.format(to)) 
        
if __name__ == "__main__":
    lap = Laptop('intel', 16, 'powerful')
    lap.browse()                              #5
    lap.work()
    lap.move('office')                        #6
    
