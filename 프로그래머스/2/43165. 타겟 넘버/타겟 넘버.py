def solution(numbers, target):
    leaves = [0]
    for n in numbers:
        tmp = []
        for l in leaves:
            tmp.append(l + n)
            tmp.append(l - n)
        leaves = tmp
    return leaves.count(target)