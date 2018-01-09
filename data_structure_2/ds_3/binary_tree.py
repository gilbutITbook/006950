class TreeNode:
    def __init__(self):
        self.__data = None
        self.__left = None
        self.__right = None

    #노드 삭제를 확인하기 위한 소멸자
    #객체가 삭제되기 전 호출된
    def __del__(self):
        print("TreeNode of {} is deleted".format(self.data))

    @property
    def data(self):  #1
        return self.__data
    
    @data.setter  #2
    def data(self, data):
        self.__data = data

    @property
    def left(self):  #3
        return self.__left

    @left.setter
    def left(self, left):  #4
        self.__left = left

    @property
    def right(self):  #5
        return self.__right

    @right.setter
    def right(self, right):  #6
        self.__right = right
    
class BinaryTree:
    def __init__(self):
        #멤버는 루트 노드를 가리키는 root 하나입니다.
        self.root = None

    #root 노드 반환
    def get_root(self):
        return self.root

    #root 노드 설정
    def set_root(self, r):
        self.root = r

    #새로운 노드를 만들어 반환합니다.
    def make_node(self):
        new_node = TreeNode()
        return new_node

    #노드의 데이터 반환
    def get_node_data(self, cur):
        return cur.data

    #노드의 데이터 설정
    def set_node_data(self, cur, data):
        cur.data = data

    #왼쪽 서브 트리 반환
    def get_left_sub_tree(self, cur):
        return cur.left

    #오른쪽 서브 트리 반환
    def get_right_sub_tree(self, cur):
        return cur.right

    #왼쪽 서브 트리를 만듭니다.
    def make_left_sub_tree(self, cur, left):
        cur.left = left

    #오른쪽 서브 트리를 만듭니다.
    def make_right_sub_tree(self, cur, right):
        cur.right = right

    #전위 순회로 트리를 순회
    #인자 (cur : 방문 노드, func : 데이터 처리 함수) 
    def preorder_traverse(self, cur, func):
        #탈출 조건
        #방문한 노드가 빈 노드일 때 
        if not cur:
            return

        #먼저 방문 노드의 데이터를 인자로
        #함수 호출
        func(cur.data)
        #왼쪽 서브 트리를 순회한다
        self.preorder_traverse(cur.left, func)
        #오른쪽 서브 트리를 순회한다 
        self.preorder_traverse(cur.right, func)

    #중위 순회로 트리를 순회
    #인자 (cur : 방문 노드, func : 데이터 처리 함수)
    def inorder_traverse(self, cur, func):
        #탈출 조건
        #방문한 노드가 빈 노드일 때
        if not cur:
            return

        #먼저 왼쪽 서브 트리를 순회한다
        self.inorder_traverse(cur.left, func)
        #왼쪽 서브 트리를 모두 순회한 후
        #방문 노드의 데이터를 인자로
        #함수 호출
        func(cur.data)
        #오른쪽 서브 트리를 순회한다
        self.inorder_traverse(cur.right, func)

    #후위 순회로 트리를 순회
    #인자 (cur : 방문 노드, func : 데이터 처리 함수)
    def postorder_traverse(self, cur, func):
        #탈출 조건
        #방문한 노드가 빈 노드일 때
        if not cur:
            return

        #왼쪽 서브 트리를 순회한다
        self.postorder_traverse(cur.left, func)
        #오른쪽 서브 트리를 순회한다
        self.postorder_traverse(cur.right, func)
        #왼쪽, 오른쪽 서브 트리를 모두 순회한 후
        #마지막으로 방문 노드의 데이터를 인자로
        #함수 호출
        func(cur.data)

if __name__ == "__main__":
    #이진 트리 객체 생성
    bt = BinaryTree()            #7

    #노드 생성
    #이진 트리 객체를 통해 노드를 생성
    n1 = bt.make_node()          #8
    #노드 데이터 설정
    #마찬가지로 이진 트리 객체를 통해
    #노드의 데이터를 설정
    bt.set_node_data(n1, 1)      #9

    n2 = bt.make_node()
    bt.set_node_data(n2, 2)

    n3 = bt.make_node()
    bt.set_node_data(n3, 3)

    n4 = bt.make_node()
    bt.set_node_data(n4, 4)

    n5 = bt.make_node()
    bt.set_node_data(n5, 5)

    n6 = bt.make_node()
    bt.set_node_data(n6, 6)

    n7 = bt.make_node()
    bt.set_node_data(n7, 7)

    #노드 1을 루트 노드로 설정
    bt.set_root(n1)

    #루트 노드의 왼쪽 자식 노드로 노드 2 설정
    bt.make_left_sub_tree(n1, n2)
    #루트 노드의 오른쪽 자식 노드로 노드 3 설정
    bt.make_right_sub_tree(n1, n3)

    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)

    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)


    #방문 노드의 데이터를 출력하는 람다 함수
    f = lambda a: print(a, end='  ') 

    #전위 순회
    #기대 출력 값 : 1  2  4  5  3  6  7
    bt.preorder_traverse(bt.get_root(), f)
    print()

    #중위 순회
    #기대 출력 값 : 4  2  5  1  6  3  7
    bt.inorder_traverse(bt.get_root(), f)
    print()

    #후위 순회
    #기대 출력 값 : 4  5  2  6  7  3  1
    bt.postorder_traverse(bt.get_root(), f)
    print()
    
    
