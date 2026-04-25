from collections import deque
def solution(begin, target, words):
    
    # 변환 가능한지 확인하는 함수
    def can_transform(w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                
        return diff == 1
    
    if target not in words:
        return 0
    
    q = deque([(begin, 0)]) # word, depth
    visited = [False] * len(words)
    
    while(q):
        cur, depth = q.popleft()
        if cur == target:
            return depth
        for i, word in enumerate(words):
            if not visited[i] and can_transform(cur, word):
                visited[i] = True
                q.append((word, depth + 1))
    
    return 0
                