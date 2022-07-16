def fib_memo(n, cache):
    if n < 3: 
        return 1
    
    if n in cache:
        return cache[n]
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    # print(cache)
    # 딕셔너리가 이렇게 바로 저장이 된다고? 

    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전 당연히 blank 이다.
    fib_cache = {}

    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
# print(fib(50))
# print(fib(100))


"""아래는 같은드 from혼코파 """
dictionary = {
    1: 1,
    2: 1
}

def fib(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fib(n-1) + fib(n-2)
        dictionary[n] = output
        return output