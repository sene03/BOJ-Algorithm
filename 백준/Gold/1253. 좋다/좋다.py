def solve():
  N = int(input())
  A = list(map(int, input().split()))
  A.sort()
  i=0;j=N-1;cnt=0;sum=0
  for idx in range(N):
    K=A[idx]
    i=0;j=N-1
    while(i<j):
      if(i==idx):
        i+=1
      if(j==idx):
        j-=1
      if(i>=j): break
        
      sum=A[i]+A[j]
      if(sum==K):
        cnt+=1
        break
      elif(sum<K):
        i+=1
      else:
        j-=1

        
  print(cnt)


if __name__=="__main__":
  solve()