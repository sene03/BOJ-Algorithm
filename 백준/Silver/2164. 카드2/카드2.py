from collections import deque
def solve():
  N = int(input())
  A = deque(range(1, N+1))
  while(len(A)>1):
    A.popleft()
    if(len(A)==1):
      break
    A.append(A.popleft())
  
  print(A.pop())

if __name__ == "__main__":
  solve()