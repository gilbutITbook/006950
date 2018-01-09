class CPU:
    pass

class RAM:
    pass

class Computer:
    def __init__(self):
        self.cpu = CPU()   #1
        self.ram = RAM()

if __name__ == "__main__":
    c = Computer()
    
