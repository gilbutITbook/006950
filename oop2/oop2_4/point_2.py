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
    
    # 더하기 연산자(+) 오버로딩
    def __add__(self, n):       #1
        x = self.x + n
        y = self.y + n
        return Point(x, y)

if __name__=="__main__":
    p1 = Point(2, 2)
    p2 = p1 + 3                #2
    #코드 7-18을 위한 코드
    #실행하면 에러가 납니다.
    #p2 = 3 + p1               #3
    
    print(p2)
