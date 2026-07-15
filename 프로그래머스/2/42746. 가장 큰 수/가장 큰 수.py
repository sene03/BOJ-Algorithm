from functools import cmp_to_key

def comparator(a,b):
    n1 = a+b
    n2 = b+a
    if n1>n2:
        return 1
    elif n1<n2:
        return -1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(reverse=True, key=cmp_to_key(comparator))
    
    answer = ''.join(numbers)
    
    return '0' if answer[0] == '0' else answer