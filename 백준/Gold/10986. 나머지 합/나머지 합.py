import sys 

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 나머지 개수 배열 초기화
    mod_arr = [0] * M
    mod_arr[0] = 1
    
    # 구간합의 나머지 배열
    D = [0] * (N+1)
    answer = 0
    
    for i in range(1, N+1):
        mod = (A[i-1] + D[i-1]) % M
        D[i] = mod # 구간합의 나머지 배열
        mod_arr[mod] += 1
    
    for mod in mod_arr:
        if mod==0: pass
        answer += mod*(mod-1)//2
    print(answer)


if __name__=="__main__":
    solve()