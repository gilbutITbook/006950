def quick_sort(data, start, end):
    #탈출 조건
    if start >= end:
        return
    
    left = start
    right = end
    pivot = data[(start + end) // 2]

    #left와 right가 교차할 때 까지 
    while left <= right:
        #left의 데이터가 pivot보다 크거나 같으면 멈춥니다.
        while data[left] < pivot:
            left+=1

        #right의 데이터가 pivot보다 작거나 같으면 멈춥니다.
        while data[right] > pivot:
            right-=1

        #left와 right가 교차하지 않았다면 교환
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    quick_sort(data, start, right)
    quick_sort(data, left, end)

if __name__ == "__main__":
    data = [2, 5, 4, 1, 8, 10, 5, 3, 6, 6, 5, 7, 9, 12, 11]
    quick_sort(data, 0, len(data) - 1)
    print(data)
