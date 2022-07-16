# Memoisation: fibonacci series
def fib_memo(n, cache):
    # recursuve function 
    # base case
    if n < 3:
        return 1
    # recursive case
    if n in cache:
        return cache[n]
        
    """
    왜 cache[n] return 먼저한 다음에 이걸 define 해 ? 
    """

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    """"
    이건 약속인가? 
    """

    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))


# Tabulation: fibonacci series

def fib_tab(n):
    # 코드를 작성하세요.
    # 리스트를 표 처럼 사용한다 
    # base case
    fib_table = [0,1,1]
    
    for i in range(3, n+1):
        fib_table.append(fib_table[i-1] + fib_table[i-2])

        #range(n+1), fib_table[i-1] + [i-2]
        #return fib_table[n]
    
    return fib_table[n]




    # Greedy Algorithm
    # 매 단계에서 가능한 가장 큰 동전을 주는 방식으로 구현한다.

    def min_coin_count(value, coin_list):
    fivehun = value // default_coin_list[1]
    value = value - (fivehun * 500)
    onehun = value // default_coin_list[0]
    value = value - (onehun * 500)
    fifty = onehun // default_coin_list[-1]
    value = value - (fifty * 500)
    ten = fifty // default_coin_list[-2]
    value = value - (ten * 500)
    # 코드를 작성하세요.
    return fivehun + onehun + fifty + ten

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))