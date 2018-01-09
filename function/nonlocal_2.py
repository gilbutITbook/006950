def outer():
    a = 2#1
    b = 3
    
    def inner():
        nonlocal a#2
        a = 100#3
    inner()
    
    print(
    "locals in outer : a = {}, b = {}".format(
    a, b))

if __name__ == "__main__":
    outer()

