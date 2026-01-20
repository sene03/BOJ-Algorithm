import sys
n,m = map(int,sys.stdin.readline().split())

sum=[0 for _ in range(n+1)] # sum[0] = 0
num = list(map(int, sys.stdin.readline().split()))

# 누적 합 배열 만들기
for i in range(1,n+1):
  sum[i] = sum[i-1] + num[i-1]

for _ in range(m):
  i,j = map(int,sys.stdin.readline().split())
  sys.stdout.write(str(sum[j] - sum[i-1]) +'\n')
