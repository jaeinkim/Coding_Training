def solution(N):
    digits_sum = sum([int(digit) for digit in str(N)]) # digit 분해 및 합

    num = N+1 # num을 기존 N보다 1 크게 하여 시작

    while True:
        if digits_sum == sum([int(digit) for digit in str(num)]):
            return num # 점점 커지는 num의 digit들 간의 합과 기준 digits_sum을 비교하여 같은 경우 num을 리턴함
        num += 1