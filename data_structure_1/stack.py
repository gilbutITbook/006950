class Stack:
    def __init__(self):
        self.container = list()#1

    def push(self, data):
        self.container.append(data)#2

    def pop(self):
        return self.container.pop()#3
        
    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def peek(self):
        return self.container[-1]#4

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    while not s.empty():
        data = s.pop()
        print(data, end = '  ')
