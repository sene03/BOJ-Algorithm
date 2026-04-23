def solution(numbers, target):
    n = len(numbers)
    ans = 0
    
    def dfs(idx, cur):
        nonlocal ans
        if (idx == n):
            if (cur == target):
                ans += 1
            return 
        
        dfs(idx+1, cur + numbers[idx])
        dfs(idx+1, cur - numbers[idx])
    
    dfs(0, 0)
    return ans