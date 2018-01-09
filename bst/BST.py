from binary_tree import *

class BST:
    #1. 이진 트리와 같음
    def __init__(self):
        self.root = None
    #2. 이진 트리와 같음
    def get_root(self):
        return self.root
    #3. 이진 트리와 같음
    def preorder_traverse(self, cur, f):
        if not cur:
            return

        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)
        
    def insert(self, data):
        #삽입할 노드 생성 및 데이터 설정
        new_node = TreeNode()
        new_node.data = data

        cur = self.root
        #루트 노드가 없을 때
        if cur == None:
            self.root = new_node
            return

        #삽입할 노드의 위치를 찾아 삽입
        while True:
            #parent는 현재 순회 중인 노드의 부모 노드를 가리킴
            parent = cur
            #삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < cur.data:
                cur = cur.left
                #왼쪽 서브 트리가 None이면 새 노드를 위치시킨다.
                if not cur:
                    parent.left = new_node
                    return
            #삽입할 데이터가 현재 노드 데이터보다 클 때
            else:
                cur = cur.right
                #오른쪽 서브 트리가 None이면 새 노드를 위치시킨다. 
                if not cur:
                    parent.right = new_node
                    return

    def search(self, target):
        cur = self.root
        
        while cur:
            #target 데이터를 찾으면 노드를 반환
            if target == cur.data:
                return cur
            #target 데이터가 노드 데이터보다 작으면
            #왼쪽 자식 노드로 이동
            elif target < cur.data:
                cur = cur.left
            #target 데이터가 노드 데이터보다 크면
            #오른쪽 자식 노드로 이동
            elif target > cur.data:
                cur = cur.right
        #while 문을 빠져나온 경우
        #target 데이터가 트리 안에 없다.
        return cur

    def __remove_recursion(self, cur, target):
        #탈출 조건 1
        #대상 데이터가 트리 안에 없다.
        if cur == None:
            return None, None
        #대상 데이터가 노드 데이터보다 작으면
        #노드의 왼쪽 자식에서 대상 데이터를 가진 노드를 지운다.(재귀 함수 호출)
        elif target < cur.data:
            cur.left, rem_node = \
                self.__remove_recursion(cur.left, target)
        #대상 데이터가 노드 데이터보다 크면
        #노드의 오른쪽 자식에서 대상 데이터를 가진 노드를 지운다.(재귀 함수 호출)
        elif target > cur.data:
            cur.right, rem_node = self.__remove_recursion(cur.right, target)
        #탈출 조건 2
        #target == cur.data    
        else:
            #1. 리프 노드일 때
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
            #2-1. 자식 노드가 하나일 때: 왼쪽 자식이 있을 때
            elif not cur.right:
                rem_node = cur
                cur = cur.left
            #2-2. 자식 노드가 하나일 때: 오른쪽 자식이 있을 때
            elif not cur.left:
                rem_node = cur
                cur = cur.right
            #3. 자식 노드가 두개일 때
            else:
                #4. 대체노드를 찾는다.
                replace = cur.left
                while replace.right:
                    replace = replace.right
                #5. 삭제 노드와 대체 노드의 값을 교환한다.
                cur.data, replace.data = replace.data, cur.data
                #6. 대체 노드를 삭제하면서 삭제된 노드를 받아온다.
                cur.left, rem_node = self.__remove_recursion(cur.left, replace.data)
        #삭제 노드가 루트 노드일 경우
        #루트가 변경될 수 있기 때문에
        #삭제 후 현재 루트를 반환 
        return cur, rem_node
                
    def remove(self, target):
        #루트 노드의 변경 가능성이 있으므로
        #루트를 업데이트 해주어야 한다.
        self.root, removed_node = self.__remove_recursion(self.root, target)
        #삭제된 노드의 자식 노드를 None으로 만든다
        removed_node.left = removed_node.right = None
        
        return removed_node

    #인자가 데이터가 아니라 노드이다.
    #insert() 메서드에서
    #노드 생성 코드만 빼면
    #코드 흐름은 완전히 같다.
    def insert_node(self, node):
        #노드 생성 코드 없음
        #노드 생성에 따른 부담을 덜 수 있다

        cur = self.root

        #insert() 메서드와 다른 점
        #new_node -> node
        if cur == None:
            self.root = node
            return

        while True:
            parent = cur
            #insert() 메서드와 다른 점
            #data->node.data
            if node.data < cur.data:
                cur = cur.left
                if not cur:
                    #insert() 메서드와 다른 점
                    #new_node -> node
                    parent.left = node
                    return
            else:
                cur = cur.right
                if not cur:
                    #insert() 메서드와 다른 점
                    #new_node -> node
                    parent.right = node
                    return

if __name__ == "__main__":
    bst = BST()
    
    #insert
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)
    
    
    f = lambda x: print(x, end = '  ')
    
    #전위 순회
    bst.preorder_traverse(bst.get_root(), f)
    print()

    #remove - 1 : 리프 노드일 때
    #bst.remove(9)
    
    #remove - 2 : 자식 노드 하나일 때
    #bst.remove(8)

    #remove - 3: 자식 노드 두 개일 때
    #bst.remove(6)

    #search
    #print("searched data : {}".format(bst.search(8).data))

    #이진 탐색 트리에서 6 노드를 삭제
    node = bst.remove(6)
    #반환 받은 삭제 노드의 데이터를 7로 변경
    node.data = 7
    #변경된 노드를 이진 탐색 트리에 다시 삽입한다 
    bst.insert_node(node)

    #기대 출력 값 : 5  3  2  4  8  7  10  9  11
    bst.preorder_traverse(bst.get_root(), f)
    print()

    
    
    
    
