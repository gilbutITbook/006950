def change_value(tu):
    tu = ('I am your father!', 2, 3, 4)#2
    return tu#3

if __name__ == "__main__":
    tu = (1, 2, 3, 4)#1
    tu = change_value(tu)#4
    print(tu)
