import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.read().split()))
arr = []
for i in range(N):
  arr.append((A[i], i)) # 처음 원소와 인덱스

arr.sort()

max_iter = -1
for i in range(N):
  # 처음 인덱스 - 나중 인덱스
  # 원소가 왼쪽으로 이동한 최대 거리 + 1
  x = arr[i][1]-i
  # print(arr[i], x)
  if(max_iter < x):
    max_iter = x

print(max_iter+1)