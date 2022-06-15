class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 

            
    def insert_after(self, preivous_node, data):
        """링크드 리스트 삽입 연산 """ 
        new_node = Node(data)

        previous_node = 

        # 가장 마지막 순서에 삽입 
        if previous_node is self.tail: 
            self.tail.next = new_node  
            self.tail = new_node 
        else: # 두 노드 사이에 삽입 
            new_node.next = previous_node.next
            previous_node.next = new_node  # why there is no 'next'  

    def prepend(self, data): 
        """ 링크드 리스트 가장 앞 삽입"""
        new_node = Node(data)
        if self.head is None:
            # self.head = new_node
            self.tail = new_node
        else: 
            # self.head.next = new_node.next  # next 가 어떻게 쓰이는지 몰랐던 듯 
            new_node.next = self.head 

        self.head = new_node  # why is it needed? 
        
    


    def find_node_with_data(self, data):
        iterator  = self.head 

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next
        
        return None 
    
    def append(self, data):
        new_node = Node(data) #what's going on here

# 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node

# 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 마지막 노드 뒤에 새로운 노드를 추가해주고 
            self.tail = new_node  # 마지막 노드를 추가한 새로운 노드로 바꿔준다 
            # 여기 마지막 노드와 그 후 마지막 노드는 다른 노드들

    def __str__(self):
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += "{} | ".format(iterator.data) # but why put  | again?
            iterator = iterator.next 
        
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


print(my_list)

node_2 = my_list.find_node_with_data(2) # index 2 에 있는 노드에 접근 
print(node_2)
my_list.insert_after(node_2, 6)

print(my_list)

head_node = my_list.head
my_list.insert_after(head_node, 9)

print(my_list)
