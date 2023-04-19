# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    snail = [[0]*i for i in range(1, n+1)]
    x  = y = angle = 0
    cnt = 1
    size = n*(n+1)//2

    while cnt <= size:
        snail[y][x] = cnt
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1

        if 0 <= ny < n and 0<= nx <= ny and snail[ny][nx] ==0:
            y, x = ny, nx
        else:
            angle = (angle+1) %3
            y += dy[angle]
            x += dx[angle]

    return [j for i in snail for j in i]

# 최적화 코드- 배열을 이렇게 받는 것이 맞을까? 메모리 초과가 적어도 백준에서는 발생할 것임
def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    y, x = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            angle = i%3
            #순서대로 아래 -> 오른쪽 -> 위 (반시계 나선형)
            if angle == 0: y += 1
            elif angle == 1: x +=1
            elif angle == 2: y-= 1; x -= 1
            res[y][x] = num
            num += 1

    return [i for j in res for i in j]

