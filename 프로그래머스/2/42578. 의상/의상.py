from collections import defaultdict
def solution(clothes):
    # clothes: [[아이템1,종류1], [아이템2,종류2], ...] 
    clothes_dict = defaultdict(list)
    for cl, cat in clothes:
        clothes_dict[cat].append(cl)
        
    res = 1
    for k, v in clothes_dict.items():
        res *= (len(v) + 1)
    
    return res - 1