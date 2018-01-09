class A:
    c_mem = 10               #1

    @classmethod
    def cls_f(cls):          #2
        print(cls.c_mem)

    def __init__(self, num):
        self.i_mem = num     #3

    def ins_f(self):
        print(self.i_mem)

if __name__ == "__main__":
    print(A.c_mem)          #4
    A.cls_f()               #5

    a = A(20)               #6
    print(a.c_mem)          #7
    a.cls_f()               #8
    

    
