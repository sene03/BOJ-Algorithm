def solution(phone_book):
    h = {num: True for num in phone_book}
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in h:
                return False
    return True

