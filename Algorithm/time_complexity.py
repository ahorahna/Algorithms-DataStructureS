### Time Complexity: O(1)

def print_first(my_list):
    print(my_list[0])

print_first([2, 3])
print_first([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])


### Time Complexity: O(n)
# case 1. O(n) function

def print_each(my_list):
    for i in range(len(my_list)):
        print(my_list[i])

# case 2. O(n) function

def print_half(my_list):
    for i in range(len(my_list) // 2):
        print(my_list[i])

"""
n 번 반복하는 게 아니라 n/2번 반복한다. 그래서 시간 복잡도는 O(1/2 n)이지만 1/2 를 버려서 
결론적으로는 0(n)이라고 할수 있다.
"""

#case 3. O(n) function

def print_three_times(my_list): 
    for i in range(len(my_list)):
        print(my_list[i])

    for i in range(len(my_list)):
        print(my_list[i])

    for i in range(len(my_list)):
        print(my_list[i])

"""
위의 코드 경우 O(3n)인데 결국에는 3을 버려서 이것도 O(n)
"""

### Time Complexity: O(n^2)
def print_pairs(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i], my_list[j])

"""
이 처럼 두 반복문 모두 인풋의 크기에 비례하는 경우, O(n^2)
"""

### Time Complexity: O(n^3)
def print_triplets(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                print(my_list[i], my_list[j], my_list[k])

"""
인풋의 크기에 비례하는 반복문이 세 번 중첩되는 경우, O(n^3)
"""

### Time Complexity: O(lg(n))
# case 1. O(lg(n)) function
def print_powers_of_two(n):
    i = 1 
    while i < n:
        print(i)
        i = i * 2 


# case 2. O(lg(n)) function
def print_powers_of_two(n):
    i = n
    while i > 1:
        print(i)
        i = i / 2


### Time Complexity: O(n * lg(n))
def print_powers_of_two_repeatedly(n):
    for i in range(n):
        j = 1
        while i < n: 
            print(i ,j)
            j = j * 2 

"""
위 코드에서 for문의 반복횟수는 nn에 비례하는데, 
while문의 반복횟수는 lg{n}lgn에 비례합니다.
while문이 for문 안에 중첩되어 있기 때문에 위 코드의 시간 복잡도는 O(n\lg{n})O(nlgn)이라고 할 수 있습니다.
"""

def print_powers_of_two_repeatedly(n):
    i = 1 
    while i < n: #반복회수: log (n)에 비례 
        for j in range(n):  #반복횟수: n 에 비례 
            print(i, j)
        i = i * 2 



###Space Complexity
# O(1)
def product(a,b,c):
    result = a * b * c
    return result

# O(n)
def get_every_other(my_list):
    every_other = my_list[::2]
    return every_other
# O(n/2)는 O(n)으로 나타낼 수 있다
 
 # O(n^2)
def largest_product(my_list):
    products = []
    for a in my_list: 
        for b in my_list:
            products.append(a * b)
    
    return max(products)

"""
 a, b 는 정수 값을 담기 때문에 O(1) 이지만 products 가 차지하는 공간은 my_list 에서 
가능한 모든 조합의 곱이 들어간다. 그래서 n^2 
"""