class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def __str__(self):
        return '({x}, {y})'.format(x = self.x, y = self.y)

if __name__=="__main__":
    p1 = Point(2, 2)
    p2 = p1 + 3            #1
print(p2)
