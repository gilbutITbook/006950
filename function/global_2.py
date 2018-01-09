g_var = 10#1

def func():
    g_var = 20#2
    print("g_var = {} in function".format(g_var))#3
    
if __name__ == "__main__":
    func()
    print("g_var = {} in main".format(g_var))#4
    
