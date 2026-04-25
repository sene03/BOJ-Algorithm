def solution(n, computers):

    visited = [False] * n
        
    def dfs(adj, visited, n, cur):
        visited[cur] = True
        
        for neighbor in range(n):
            # 연결되어 있고 방문하지 않았다면
            if adj[cur][neighbor] == 1 and not visited[neighbor]: 
                dfs(adj, visited, n, neighbor)
    
    networks = 0
    for computer in range(n):
        if not visited[computer]:
            networks += 1
            dfs(computers, visited, n, computer)
    
    return networks