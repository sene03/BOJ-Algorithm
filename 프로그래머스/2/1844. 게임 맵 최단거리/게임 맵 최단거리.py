from collections import deque
def solution(maps):
    cur = (0,0)
    d = 0
    
    n = len(maps)-1 
    m = len(maps[0])-1 
    
    dxy = [(-1,0),(1,0),(0,-1),(0,1)]
    
    q = deque([(0,0,1)]) # x, y, dist
    # visited check -> maps를 0으로 바꾸기
    maps[0][0] = 0
    
    while(q):
        cur = q.popleft()
        x, y, dist = cur
        # 목적지에 먼저 도착한 거리를 반환
        if((x,y) == (n,m)):
            return dist
        
        for dx, dy in dxy:
            nx, ny = cur[0]+dx, cur[1]+dy

            if(0 <= nx <= n and 0 <= ny <= m and maps[nx][ny] == 1):
                maps[nx][ny] = 0 # visited
                q.append((nx, ny, dist+1))
            else:
                continue
                
    return -1








