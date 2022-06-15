# 선택정렬 selection sort
# 삽입정렬 insertion sort 
# 합병정렬 merge sort

def merge(list1, list2):
    merged_list  = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1 

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


"""
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] > list2[j]:
                return merged_list.appned(list2[j], list1[i])
            return merged_list.appned(list2[i], list1[j])
 for 문을 쓰면 break를 통해서 언제 끊어줘야 하는지 + 변수 더 등이 필요하다 .? 왜 ?        

"""

def merge_sorted





# quick sort 