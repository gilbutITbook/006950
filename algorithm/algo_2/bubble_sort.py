def bubble_sort(data):
    data_len = len(data)

    for i in range(data_len - 1):           #1
        for j in range(data_len - 1 - i):   #2
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == "__main__":
    li = [2, 3, 5, 2, 3, 8, 6, 7, 10, 8, 1, 4]
    bubble_sort(li)
    print(li)


