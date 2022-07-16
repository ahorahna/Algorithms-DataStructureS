
"""
Initial code
"""
    # index = (0 + len(some_list) // 2
    # print(index)
    # if some_list[index] > element:
    #     del some_list[index: -1]
    # elif some_list[index] < element:
    #     del some_list[0:index]
    # else:
    #     return some_list[index]
        

"""
hints ->
"""
def binary_search(element, some_list):
    start_index = 0 
    end_index = len(some_list) - 1 
    
    while True 
        mid_point = (start_index + end_index) // 2
        if some_list[mid_point] == element:
            return mid_point
        elif some_list[mid_point] > element:
            end_index = mid_point - 1
        else: 
            start_index = midpoint + 1
        



def binary_search(element, some_list):
    start_index = 0 
    end_index = len(some_list) - 1 
    
    while start_index <= end_index:  #condition added
        mid_point = (start_index + end_index) // 2
        if some_list[mid_point] == element:
            return mid_point
        elif some_list[mid_point] > element:
            end_index = mid_point - 1
        else: 
            start_index = midpoint + 1
        

"""
answer_code
"""
 def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None       #return None added 
    

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
