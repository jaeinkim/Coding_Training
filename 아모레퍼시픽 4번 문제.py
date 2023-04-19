# 메모리 문제가 있을 수 있는 코드
# M, N = map(int, input().split())
# res = [[0]*N for _ in range(M)]
# x, y = 0, 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# cnt = 1
# angle = 0
#
# while cnt < M*N:
#     res[y][x] = 1
#     ny = y + dy[angle]
#     nx = x + dx[angle]
#     cnt+=1
#     if 0 <= nx < N and 0<= ny < M and res[ny][nx] == 0:
#         x, y = nx, ny
#     else:
#         angle = (angle+1)%4
#         y += dy[angle]
#         x += dx[angle]
#
# print(y+1, x+1)



####################
# 완전 탐색 방법
####################
import sys
M, N = map(int, sys.stdin.readline().split())

x, y = 1, 1
angle = 0
iter = 1
max_iter_x = N
max_iter_y = M-1
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(1, (M*N)):
    angle = angle%4
    nx = x + dx[angle]
    ny = y + dy[angle]
    if angle in (0, 2):
        if max_iter_x == iter:
            max_iter_x -= 1
            iter = 1
            angle = (angle + 1)%4
            y += dy[angle]

        else:
            iter += 1
            x = nx

    elif angle in (1,3):
        if max_iter_y == iter:
            max_iter_y -= 1
            iter = 1
            angle = (angle + 1)%4
            x += dx[angle]
        else:
            iter += 1
            y = ny
print(y, x)
