def change_value(x, value):#3
    x = value#4
    print("x : {} in change_value".format(x))

if __name__ == "__main__":
    x = 10#1
    change_value(x, 20)#2
    print("x : {} in main".format(x))

