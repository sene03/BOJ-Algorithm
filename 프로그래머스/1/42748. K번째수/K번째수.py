def solution(array, commands):
    ans = []
    for i,j,k in commands:
        arr = array[i-1:j]
        arr.sort()
        ans.append(arr[k-1])
    return ans
