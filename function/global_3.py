g_var = 10#1

def func():
    global g_var#2
    g_var = 20#3

if __name__ == "__main__":
    print("g_var : {} before".format(g_var))
    func()
    print("g_var : {} after".format(g_var))
