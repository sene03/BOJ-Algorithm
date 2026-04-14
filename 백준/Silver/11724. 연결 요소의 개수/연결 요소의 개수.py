import sys
N,M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
  u,v = map(int, sys.stdin.readline().split())
  adj[u].append(v)
  adj[v].append(u)

visited = [False]*(N+1)

def dfs(start_node):
  stack = [start_node]
  visited[start_node] = True
  
  while stack:
    curr = stack.pop()
    
    for neighbor in adj[curr]:
      if not visited[neighbor]:
        visited[neighbor] = True
        stack.append(neighbor)

count = 0
for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    count += 1
    
print(count)
