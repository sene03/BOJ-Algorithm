
def solve():
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    A.sort()
    left=0; right=N-1; cnt=0; sum=0
    while(left < right):
        sum = A[left] + A[right]
        if(sum == M): 
            cnt+=1
            left+=1
            right-=1
        elif(sum < M):
            left+=1
        else:
            right-=1
    print(cnt)
    
if __name__=="__main__":
    solve()