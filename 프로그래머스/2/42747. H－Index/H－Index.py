def solution(citations):
    citations.sort()
    n = len(citations)
    h = 0
    
    for i, c in enumerate(citations):
        if c >= (n-i):
            h = n-i
            break
    return h