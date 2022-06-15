class Node:
    """ 링크드 리스트의 노드 클라스 """

    def __init__(self, data):
        self.data = data #노드가 저장하는 데이터
        self.next = None # 다음 노드에 해당하는 레퍼런스 
    
# 데이터 2, 3, 5, 7, 11 을 담는 노드들 생성 (노드 인스턴스 생성)
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
trail_node = Node(11)

# 인스턴스.속성 을 class 밖에서 접근 할 수 있나?

# 노드들을 연결 
head_node.next = node_1
node_1.next = node_2 
node_2.next = node_3
node_3.next = trail_node

# 노드 순서대로 출력 
iterator = head_node

while iterator is not None: # tail_node의 next 속성이  None 이기 때문에 tail_node 다음에는 iterator 가 None 으로 바뀜.
    print(iterator.data)
    iterator = iterator.next

print('-----node created-------')

class LinkedList:
    """ 링크드 리스트 클라스"""
    """ 링크드 리스트는 속성을 두 가지만 가진다. (1) head node (2) tail node """

    def __init__(self):
        self.head = None # 왜 None 으로 설정하지?? 
        self.tail = None

    def find_node_at(self, index):
        """ 링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for i in range(index):
            iterator = iterator.next 

        return iterator

    """ 추가 연산은 append operation 이라고 합니다""" # append what where ? ? 
    def append(self, data):
        """ 링크드 리스트 추가 연산 메소드""" 
        new_node = Node(data)

        if self.head is None: # 링크드 리스트가 비어있는 경우 
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node # 가장 마지막 노드에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다 


    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""        
        res_str = '|'

        iterator = self.head

        # # 링크드 리스트를 끝까지 돈다 
        while iterator is not None: 
        #     # 각 노드의 데이터를 리턴하는 문자열에 더해준다. 
            res_str += f"{iterator.data} |"
            iterator = iterator.next # 다음 노드로 넘어간다 

        return res_str


# 새로운 링크드 리스트 생성 
my_list = LinkedList()

# 링크드 리스트에 데이터 추가 
"""링크드 리스트 하나를 생성해서 my_list에 지정했고, 거기에 2,3,5,7,11을 추가했다.
즉 my_list에는 노드 다섯 개가 있고 그 각각의 노드들엔 2,3,5,7,11 이 ㄲ각 저장되어있다""" 

my_list.append(2) 
my_list.append(3) 
my_list.append(5) 
my_list.append(7) 
my_list.append(11)

# 실제로 잘 저장 되었는 지 확인
iterator = my_list.head

while iterator is not None: 
    print(iterator.data)
    iterator = iterator.next

print(my_list)



# 링크드 리스트 노드에 접근(데이터 가져오기)
print(my_list.find_node_at(3).data)

# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13

 # 전체 링크드 리스트 출력
print(my_list)
