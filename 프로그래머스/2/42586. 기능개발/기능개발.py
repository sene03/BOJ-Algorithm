import math
def solution(progresses, speeds):
    ans = []
    days = []
    
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    
    cnt = 1
    max_day = days[0] # 배포 그룹 내에서 가장 큰 일수
    for i in range(1, len(days)):
        if days[i] <= max_day:
            cnt += 1
        else:
            max_day = days[i]
            ans.append(cnt)
            cnt = 1
    
    ans.append(cnt)
    return ans