######################################
# 첫번째 시도. 시간 초과 발생
######################################
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

res = [[0]*N for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x = 0
y = 0
ax = 0
ay = 0
num = N*N
iter = 0
angle = 0
max_iter_x = N-1
max_iter_y = N
for i in range(num):
    res[y][x] = num - i
    if res[y][x] == M:
        ax = x + 1
        ay = y + 1
    nx = x + dx[angle]
    ny = y + dy[angle]
    iter += 1
    if angle in (1, 3):
        if iter == max_iter_x:
            angle = (angle+ 1)%4
            iter = 0
            max_iter_x -= 1
            y += dy[angle]
        else:
            x = nx
            y= ny
    elif angle in (0, 2):
        if iter == max_iter_y:
            angle = (angle+ 1)%4
            iter = 0
            max_iter_y -= 1
            x += dx[angle]
        else:
            x = nx
            y= ny
c = 0
s = ''
for k in [j for i in res for j in i]:
    c+=1
    s += str(k) + ' '

    if c%N == 0: s+= '\n'
print(s.strip())
print(ay, ax)


######################################
# 두번째 시도. 통과!!!
######################################
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

res = [[0]*N for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x = 0
y = 0
ax = 0
ay = 0
num = N*N
iter = 0
angle = 0
max_iter_x = N-1
max_iter_y = N
for i in range(num):
    res[y][x] = str(num - i)
    if res[y][x] == str(M):
        ax = x + 1
        ay = y + 1
    nx = x + dx[angle]
    ny = y + dy[angle]
    iter += 1
    if angle in (1, 3):
        if iter == max_iter_x:
            angle = (angle+ 1)%4
            iter = 0
            max_iter_x -= 1
            y += dy[angle]
        else:
            x = nx
            y= ny
    elif angle in (0, 2):
        if iter == max_iter_y:
            angle = (angle+ 1)%4
            iter = 0
            max_iter_y -= 1
            x += dx[angle]
        else:
            x = nx
            y= ny
c = 0
s = ''
for k in res:
    print(' '.join(k))
print(ay, ax)