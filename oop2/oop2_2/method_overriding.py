class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print('{} can not do anything else'.format
              (self.name))
    #나머지 메서드

class Car:
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)
        
    def drive(self):                #1
        self.owner.concentrate()    #2
        print('{} is driving now.'.format(self.owner.name))   #3

class SelfDrivingCar(Car):
    def drive(self):                #4
        print('Car is driving by itself')   #5

    #나머지 메서드

if __name__ == "__main__":
    car = Car('Greg')
    car.drive()             #6
    print('')

    s_car = SelfDrivingCar('John')
    s_car.drive()           #7
    
    
        
    
