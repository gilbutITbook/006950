def linear_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:    #1
            return idx
    return None

if __name__ == "__main__":
    data = [i ** 2 for i in range(1, 11)]

    target = 9
    idx = linear_search(data, target)

    if idx == None:
        print("{}이 존재하지 않습니다".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {} 입니다.".format(idx, data[idx]))

    
