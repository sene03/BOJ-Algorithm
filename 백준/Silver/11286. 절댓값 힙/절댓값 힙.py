from queue import PriorityQueue
import sys

que = PriorityQueue()
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.read().split()))
print = sys.stdout.write

for i in range(N):
  if(A[i]==0):
    if(que.empty()):
      print('0\n')
    else:
      print(str(que.get()[1])+'\n')
  else: # put
    que.put((abs(A[i]), A[i])) 