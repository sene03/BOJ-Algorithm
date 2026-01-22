import sys
n, m = map(int, sys.stdin.readline().split())
num=[[0] * (n+1)] # 1행 0으로 초기화
sum=[[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
  row = [0] + list(map(int, sys.stdin.readline().split()))
  num.append(row)

for i in range(1,n+1):
  for j in range(1,n+1):
    sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + num[i][j]

for _ in range(m):
  x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
  result = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]
  sys.stdout.write(str(result)+'\n')