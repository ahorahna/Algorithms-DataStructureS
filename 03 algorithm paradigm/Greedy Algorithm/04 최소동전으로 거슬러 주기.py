#  손부끄러운 내 풀이
def min_coin_count(value, coin_list):
    one = value // 500
    value = value - 500 * one
    two = value // 100
    value = value - 100 * two
    three = value // 50
    value = value - 50 * three
    four = value //10
    value = value - 10 * four
    
    return one + two + three + four
    


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))


# 모범답안
def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list 의 값을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value//coin)

        # 잔액을 계산한다
        value %= coin

    return count