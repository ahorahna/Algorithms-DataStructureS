def merge(list1, list2):
    merged_list = []
    
    i = 0 
    j = 0 
    
    while i < len(list1) and j < len(list2): 
        ## 왜 while 함수를 여기 쓰는지 다시 상기. 
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가    
    # 내가 놓친 블럭     
    if i == len(list1):
        merged_list += list2[j:]

     # list1에 남은 항목이 있으면 정렬 리스트에 추가    
    elif j == len(list2):
        merged_list += list1[i:]
        
    return merged_list
    
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))