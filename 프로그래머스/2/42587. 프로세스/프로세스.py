from collections import deque
def solution(priorities, location):
    q = deque([(i, p) for i, p in enumerate(priorities)])
    
    i = 0
    while q:
        cur = q.popleft()
        
        # find max priority
        if any(cur[1] < item[1] for item in q):
            q.append(cur)  
        else:
            # 실행
            if location == cur[0]:
                return i + 1
            i += 1
        
        
        