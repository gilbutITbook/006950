def fibonacci(n):   #1
    if n == 1:      #2
        return 0
    elif n == 2:    #3
        return 1

    return fibonacci(n-2) + fibonacci(n-1)  #4

if __name__ == "__main__":
    n = 10
    for i in range(1, n+1):
        print(fibonacci(i), end = '  ')

