class Person:
    def __init__(self, name, age):          #1
        self.name = name
        self.age = age
    @classmethod
    def init_from_string(cls, string):     #2
        '''
        string format : '<name>_<age>'
        '''
        name, age = string.split('_')
        return cls(name, int(age))         #3

if __name__ == "__main__":
    p = Person.init_from_string('greg_30') #4
    print(p.name)
    print(p.age)
    
