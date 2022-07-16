# 선형 탐색 Linear Search 
def linear_search(list, value):
    for element in list:
        if element == value:
            return value
    return None
# Time Complexity: O(n)


# 이진 탐색 Binary Search 
def binary_search(element, some_list):
    start_index = 0 
    end_index = len(some_list) - 1
    
    while start_index <= end_index: 
        mid_index = (start_index + end_index) // 2
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] > element:
            end_index = mid_index - 1 
        else: 
            start_index = mid_index + 1
            
    return None

# 여기서 return 이 없는 부분 다시 봐야됨 
# Time Complexity: O(lg(n))


# 이진 탐색 Binary Search with Recursio 




# 이진 탐색 my first trial 

def binary_search(element, some_list):
    start_index = 0
    last_index = len(some_list) - 1
    
    while start_index <= last_index:
        mid_index = (start_index + last_index) // 2 
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] < element:
            start_index = mid_index + 1 
        else:
            last_index = mid_index - 1
        
    return None
            

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


# 이진 탐색 재귀로 구현해보기 

"""
반드시 재귀(recursion)의 개념을 사용하셔야 합니다. 
코드 구현이 꽤 어려우니, 천천히 고민해 보시기 바랍니다. 
다른 재귀 문제를 풀 때와 마찬가지로 base case와 recursive case를 생각해 내는 것이 핵심입니다!
"""

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    if start_index > end_index: 
        return None 
        
    mid_index = (start_index + end_index) // 2
    
    if some_list[mid_index] == element:
        return mid_index
    elif some_list[mid_index] < element:
        return binary_search(element, some_list, start_index = mid_index + 1, end_index = None)
    else: 
        return binary_search(element, some_list, start_index, end_index = mid_index - 1 )
        
    