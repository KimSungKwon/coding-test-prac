'''
2중 for문은 시간초과
문자열 정렬을 이용해서 인접하는 문자열만 확인해야 함
'''


def solution(phone_book):
    phone_book = sorted(phone_book)   # 문자열 정렬은 앞글자부터 사전순으로 정렬됨

    for i in range(len(phone_book) - 1):
        target = phone_book[i]
        if target in phone_book[i+1][0:len(target)]:  # 정렬했기때문에 바로 다음 문자열을 확인하면 됨
            return False
    return True
