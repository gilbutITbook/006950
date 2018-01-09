class Queue:
    def __init__(self):
        self.container = list()        #1

    def enqueue(self, data):           #2
        self.container.append(data)
    
    def dequeue(self):
        return self.container.pop(0)   #3

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def peek(self):
        return self.container[0]      #4

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue(), end = '  ')
