def solution(numbers):
    numbers = list(map(str, numbers))
    
    # '9' > '998' 을 만들기 위해서 '999'와 '989898'을 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    ans = ''.join(numbers)
    
    return '0' if ans[0] == '0' else ans
    