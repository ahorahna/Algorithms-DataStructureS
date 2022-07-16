# Recursive Function 
# 모두 반복문을 쓰지 말고 재귀의 개념을 활용할 것. 

# 01. Fibonacci sequence 
# n번째 피보나치 수를 리턴
def fib(n):
    if n < 3:
        return 1 
    return fib(n - 1) + fib(n - 2)
    

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
    

# 02. Triangle number
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:
        return n
    
    return triangle_number(n-1) + n 
    

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))


# 03. 자릿수 합 
# hint.  12345 의 자릿수 합을 구하기 위해서는, 가장 마지막 자릿수인 5에 1234의 자릿수의 합을 더해주면 된다.
# 1234의 자릿수 합을 구하는 문제는 많이 익숙한 형태다...!! 
# c.f. python operation / division // floor division 정수 몫 % modulus 나머지 

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n // 10) + (n % 10) 

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# 04. 리스트 뒤집기


# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
        
    return some_list[-1:] + some_list[:-1]
    # 코드를 입력하세요.

# 05. binary search algorithm using recursive function 

# 06. Hanoi's top 
