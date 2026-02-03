def solve():
  S, P = map(int, input().split())
  arr = list(input())
  min_count_arr = list(map(int, input().split()))
  
  min_count = {
    'A': min_count_arr[0],
    'C': min_count_arr[1],
    'G': min_count_arr[2],
    'T': min_count_arr[3],
  }
  dna_cnt = {"A":0, "G":0, "C":0, "T":0}
  i=0; j=P-1; ans=0;
  
  # 일단 먼저 세기
  for idx in range(P):
    dna_cnt[arr[idx]]+=1

  while(j<=S-1):
    flag=True
    for dna in ['A', 'C', 'G', 'T']:
      if dna_cnt[dna] < min_count[dna]:
        flag=False
        break
    if(flag):
      ans+=1
    i+=1; j+=1; # move the sliding window
    if(j>S-1): break
  
    # update dna_cnt
    dna_cnt[arr[i-1]]-=1
    dna_cnt[arr[j]]+=1
  
  print(ans)


if __name__=="__main__":
  solve()