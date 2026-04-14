import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
  a,b=map(int, sys.stdin.readline().split())
  adj[a].append(b)
  adj[b].append(a)
  


def dfs(start):
  res = []
  # To visit nodes in ascending order, 
  # sort adjecency list in reverse order
  for l in adj:
    l.sort(reverse=True)

  visited = [False]*(n+1)
  
  s = [start]
  
  while(s):
    cur = s.pop()
    
    if not visited[cur]:
      visited[cur] = True
      res.append(cur)
      for i in adj[cur]:
        if not visited[i]:
          s.append(i)
      
  res = map(str, res)
  sys.stdout.write(" ".join(res))


def bfs(start):
  res = []
  for l in adj:
    l.sort()

  visited = [False]*(n+1)
  
  dq = deque([start])

  while(dq):
    cur = dq.popleft()
    
    if not visited[cur]:
      visited[cur] = True
      res.append(cur)
      for i in adj[cur]:
        if not visited[i]:
          dq.append(i)

  res = map(str, res)
  sys.stdout.write(" ".join(res))
  

dfs(v)
print()
bfs(v)