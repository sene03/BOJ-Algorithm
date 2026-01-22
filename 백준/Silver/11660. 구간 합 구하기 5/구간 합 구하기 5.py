import sys

def solve():
    # 모든 입력을 한 번에 읽어와서 공백 단위로 분리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    input_ptr = 0
    
    n = int(input_data[input_ptr])
    m = int(input_data[input_ptr + 1])
    input_ptr += 2
    
    # 2차원 누적 합 배열 초기화 (N+1 x N+1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 데이터 입력 및 누적 합 계산
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = int(input_data[input_ptr])
            # 점화식: 현재 위치까지의 합 = 위 + 왼쪽 - 대각선왼쪽위 + 현재값
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + val
            input_ptr += 1
            
    # 결과 출력을 위한 리스트
    output = []
    for _ in range(m):
        x1 = int(input_data[input_ptr])
        y1 = int(input_data[input_ptr + 1])
        x2 = int(input_data[input_ptr + 2])
        y2 = int(input_data[input_ptr + 3])
        input_ptr += 4
        
        # 구간 합 계산
        res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        output.append(str(res))
    
    # 한꺼번에 출력
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()