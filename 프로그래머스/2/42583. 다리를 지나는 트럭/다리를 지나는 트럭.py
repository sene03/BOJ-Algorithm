from collections import deque
def solution(bridge_length, weight, truck_weights):
    # truck_weights 큐로 만들기
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    t = 0	
    s = 0
    
    while bridge:
        t += 1
        s -= bridge.popleft()
        if waiting:
            if s + waiting[0] <= weight:
                truck = waiting.popleft()
                bridge.append(truck)
                s += truck
            else:
                bridge.append(0)

    return t

