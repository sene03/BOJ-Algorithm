import sys

def solve():
  N = int(input())
  A = list(map(int, sys.stdin.read().split()))
  
  A.sort()
  for a in A:
    sys.stdout.write(str(a)+"\n")

if __name__=="__main__":
  solve()