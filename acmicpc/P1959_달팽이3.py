# # 메모리 초과 발생
# M, N = map(int, input().split())
# res = [[0]*N for _ in range(M)]
# x, y = 0, 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# cnt = 1
# rotate_cnt = 0
# angle = 0
#
# while cnt < M*N:
#     res[y][x] = 1
#     ny = y + dy[angle]
#     nx = x + dx[angle]
#     cnt+=1
#     # print(f'ny, nx = {ny, nx}')
#     if 0 <= nx < N and 0<= ny < M and res[ny][nx] == 0:
#         x, y = nx, ny
#         # print(f'here? y, x = {y, x}')
#     else:
#         angle = (angle+1)%4
#         rotate_cnt +=1
#         y += dy[angle]
#         x += dx[angle]
#         # print(f'here2? y, x = {y, x}')
#
# print(rotate_cnt)
# print(y+1, x+1)



####################
# 두번째 시도, 시간 초과
####################
# import sys
# M, N = map(int, sys.stdin.readline().split())
#
# x, y = 1, 1
# angle = 0
# iter = 1
# max_iter_x = N
# max_iter_y = M-1
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# rotate_cnt = 0
#
# for i in range(1, (M*N)):
#     angle = angle%4
#     nx = x + dx[angle]
#     ny = y + dy[angle]
#     # print(f'x, y = {x, y}')
#     # print(f'nx, ny = {nx, ny}')
#     # print(f'max_iter_x = {max_iter_x}')
#     # print(f'max_iter_y = {max_iter_y}')
#     # print(f'iter = {iter}')
#     # print(f'angle = {angle}')
#     if angle in (0, 2):
#         if max_iter_x == iter:
#             max_iter_x -= 1
#             iter = 1
#             rotate_cnt += 1
#             angle = (angle + 1)%4
#             y += dy[angle]
#             # print(f'here1 ')
#
#         else:
#             iter += 1
#             x = nx
#             # print(f'here2 ')
#
#     elif angle in (1,3):
#         if max_iter_y == iter:
#             max_iter_y -= 1
#             iter = 1
#             rotate_cnt += 1
#             angle = (angle + 1)%4
#             x += dx[angle]
#             # print(f'here3 ')
#
#         else:
#             iter += 1
#             y = ny
#             # print(f'here4 ')
#     # print(f'i = {i}')
# print(rotate_cnt)
# print(y, x)
#

#####
# 세 번째 시도
import sys
M, N = map(int, sys.stdin.readline().split())

if M > N: print((N-1)*2+1)
elif M <= N: print((M-1)*2)

if M == N:
    if M%2 == 1 and N%2 ==1:
        print((M//2)+1, (N//2)+1)
    elif M%2 == 0 and N%2 ==0:
        print((M//2)+1, (N//2))

elif M > N:
    if N%2 == 0:
        print((N//2)+1, (N//2))
    elif N%2 == 1:
        print((N//2)+1+(M-N), (N//2)+1)

elif M < N:
    if M%2 == 0:
        print((M//2)+1, (M//2))
    elif M%2 == 1:
        print((M//2)+1, (M//2)+1+(N-M))
