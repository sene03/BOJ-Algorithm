import sys

def solve():
  N = int(sys.stdin.readline())
  A = []
  for _ in range(N):
    A.append(int(sys.stdin.readline()))

  i=0
  stack=[]
  result=[]
  for num in range(1, N+1):
    if(num<=A[i]):
      stack.append(num)
      result.append('+')
    while(stack and stack[-1]==A[i]):
      stack.pop()
      i+=1
      result.append('-')
  
  if(stack): 
    sys.stdout.write("NO")
  else:
    sys.stdout.write('\n'.join(result))


if __name__=="__main__":
  solve()