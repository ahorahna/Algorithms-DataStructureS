def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
countdown(4)

# task1 Fibonacci Numbers 

#n번째 피보나치 수를 리턴
def fib(n):
    if n < 3:
        return 1 
    return fib(n-2) + fib(n-1)


# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

# task2 Triangle Number 

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:
        return n
    return triangle_number(n - 1) + n
    # 코드를 입력하세요

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
