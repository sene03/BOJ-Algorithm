from collections import deque

def solve():
  N, L = map(int, input().split())
  A = list(map(int, input().split()))
  D = deque([]) # deque for sliding window

  start=-L+1; end=0;
  
  # push
  D.append([end, A[end]]) # [idx, value]
  while(end!=N):
    # print(f'start: {start}, end: {end}, min: {D[0][1]}', D)
    # first value of deque is the minimum
    print(D[0][1], end=" ")
    
    # move the window
    start+=1; end+=1;
    if(end==N): break
    # deque의 마지막 값이 새로 들어올 값보다 크다면
    while(D and D[-1][1] > A[end]): 
      D.pop() # 마지막 값 제거하기
    D.append([end, A[end]]) # 새로 들어온 값 넣기
    # 맨 처음 값 꺼내기
    if(D[0][0]<start): D.popleft()
    
    
  
if __name__=="__main__":
  solve()