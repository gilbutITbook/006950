a = 1

def outer():
    b = 2
    c = 3
    print(a, b, c)#1
    def inner():
        d = 4
        e = 5
        print(a, b, c, d, e)#2
    inner()

if __name__ == "__main__":
    outer()
