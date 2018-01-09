class Node:
    def __init__(self, data=None):
        #노드는 데이터 부분과
        #다음 노드를 가리키는 참조 부분을 가진다 
        self.__data = data
        self.__next = None

    #노드 삭제를 확인하기 위한 코드 
    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n

class Linked_list:
    def __init__(self):
        #연결 리스트의 첫번째 노드를 가리킴
        self.head = None
        #연결 리스트의 마지막 노드를 가리킴
        self.tail = None
        #데이터의 개수
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def append(self, data):
        #삽입할 노드를 만든다
        new_node = Node(data)               #1

        #첫번째 경우
        #리스트가 비어 있을 때
        if self.empty():                    #2
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
        #데이터가 한 개 이상 있을 때  
        else:                               #3
            self.tail.next = new_node       #4
            self.tail = new_node            #5
            self.d_size += 1

    def search_target(self, target, start = 0):
        '''
        search_target(target, start = 0) -> (data, pos)
        start로 부터 target과 일치하는 첫번째 데이터와 그 위치를 반환
        target 존재하지 않을 때 : -> (None, None)
        '''
        if self.empty():
            return None
        #첫번째 노드를 가리킨다
        pos = 0
        #노드의 순회 코드
        cur = self.head                             #6
        #pos가 탐색 시작 위치 start보다 클 때만
        #대상 데이터와 현재 노드의 데이터를 비교
        if pos >= start and target == cur.data:     #8
            return cur.data, pos                    #10
        
        while cur.next:
            pos += 1
            #노드의 순회 코드
            #cur가 노드의 next를 통해 다음 노드로 이동
            cur = cur.next                                #7
            #pos가 탐색 시작 위치 start보다 클 때만
            #대상 데이터와 현재 노드의 데이터를 비교
            if pos >= start and target == cur.data:     #9
                return cur.data, pos                    #11
            
        return None, None          

    def search_pos(self, pos):
        '''
        search_pos(pos)->data
        pos가 범위를 벗어날 때 -> None
        '''
        #pos가 범위를 벗어나면
        #None을 반환
        if pos > self.size() - 1:                       #14
            return None
        
        
        cnt = 0
        cur = self.head                                 #12
        if cnt == pos:                                  
            return cur.data                             

        #cnt가 pos와 같아질 때
        #순회를 멈춘다
        while cnt < pos:                                #15
            cur = cur.next                              #13
            cnt += 1

        return cur.data                                 #16

    def remove(self, target):
        if self.empty():
            return None

        #before는 current 노드의 이전 노드를 가리킨다
        #삭제할 때 요긴하게 쓰인다 
        bef = self.head                      #17 
        cur = self.head
        #A. 삭제 노드가 첫 번째 노드일 때 
        if target == cur.data:
            #A-1. 데이터가 하나일 때
            if self.size() == 1:
                self.head = None
                self.tail = None
            #A-2. 데이터가 두 개 이상일 때 
            else:
                self.head = self.head.next
            self.d_size -= 1
            return cur.data
        
        while cur.next:
            bef = cur
            cur = cur.next
            #B. 삭제 노드가 첫 번째 노드가 아닐 때 
            if target == cur.data:
                #B-1. 삭제 노드가 마지막 노드일 때 
                if cur == self.tail:
                    self.tail = bef
                #B-2. 일반적인 경우
                bef.next = cur.next         #18
                self.d_size -= 1
                return cur.data
            
        return None

def show_list(slist):
    if slist.empty():
        print('The list is empty')
        return
    
    for i in range(slist.size()):
        print(slist.search_pos(i), end = '  ')

if __name__ == "__main__":
    slist = Linked_list()
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print()
    
    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)         
    slist.append(10)
    slist.append(7)
    slist.append(2)     
    
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print()
    
    data1, pos1 = slist.search_target(2)    
    if data1:
        print('searched data : {} at pos<{}>'.format(data1, pos1))
    else:
        print('there is no such data')

    data2, pos2 = slist.search_target(2, pos1 + 1)      
    if data2:
        print('searched data : {} at pos<{}>'.format(data2, pos2))
    else:
        print('there is no such data')

            
    
    if slist.remove(2):
        print("데이터의 개수 : {}".format(slist.size()))
        show_list(slist)
        print()
    else:
        print('target Not found')

    if slist.remove(2):
        print("데이터의 개수 : {}".format(slist.size()))
        show_list(slist)
        print()
    else:
        print('target Not found')

    slist.append(17)
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print()
    
    
    
    
