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
    if i == len(list1): ### 내가 놓친 블럭 
        merged_list += list2[j:]

     # list1에 남은 항목이 있으면 정렬 리스트에 추가    
    elif j == len(list2):
        merged_list += list1[i:]
        
    return merged_list


# 합병 정렬
# divide and conquer 방법으로
def merge_sort(my_list):
#     base case
    if len(my_list) < 2:
        return my_list 
    
    left_half = my_list[:len(my_list)//2]
    print(left_half)
    right_half = my_list[len(my_list)//2:]
    print(right_half)

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left_half), merge_sort(right_half))
    
    
    # 코드를 입력하세요.

# 테스트
# print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
# print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
