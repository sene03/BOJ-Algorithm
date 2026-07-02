def solution(s):
    l = 0
    for a in s:
        if a == '(':
            l += 1
        else:
            l -= 1
        if l < 0:
            return False

    if l == 0:
        return True
    else:
        return False