# 1. 시간 초과 발생
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True
# 기준 키가 정해졌으면 해당 키 길이보다 작은 것은 제외하고 비교해야 함. 즉, 더 긴것만 비교해야 함

# 2. 시간 초과 발생
def solution(phone_book):
    for j in range(len(phone_book)):
        for k in range(len(phone_book)):
            if phone_book[j].startswith( phone_book[k]) and j != k:
                return False
    return True

# 3. 책의 풀이 첫번째
def solution(phone_book):
    headers = {}

    for phone_number in phone_book:
        headers[phone_number] = 1

    for phone_number in phone_book:
        header = ''
        for number in phone_number:
            header += number
            if header in headers and header != phone_number:
                return False
    return True

# 4. 책의 풀이 두 번째
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1): return False
    return True
