def merge(list1, list2):
    
    merged_list = []
    
    for i in list1:
        for j in list2:
            if i < j:
                merged_list.append(i)
            else:
                merged_list.append(j)
                
    
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))