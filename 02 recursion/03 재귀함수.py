# task3 Sum Digits
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n < 10:
        return n 
    return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# Time Complexity; O(d) 

# task4
# flip a list
아마 리스트 공부 ㅠ 

def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


# task5 Hanoi's top 
하노이의 탑 질문 있음

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case: 옮길 원판이 없으면 부분 문제를 나누지 않고 함수를 끝낸다
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        
        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)
        
        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)
        
        # 3. 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)

# 테스트
hanoi(3, 1, 3)
