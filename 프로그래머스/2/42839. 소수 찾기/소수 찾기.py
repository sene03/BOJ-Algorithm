from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

def solution(numbers):
    set_numbers = set()
    for r in range(1, len(numbers) + 1):        
        for p in permutations(numbers, r):
            set_numbers.add(int(''.join(p)))
    
    cnt=0
    for n in set_numbers:
        if is_prime(n):
            cnt+=1
    return cnt
    
    
    
    
    
    
    
    