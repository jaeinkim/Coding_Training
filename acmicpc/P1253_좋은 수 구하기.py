#책의 코드
import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N-1
    while i < j: # 투 포인터 알고리즘
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result +=1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(Result)

# 나의 코드
n = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

if n <3:
    print(0)

else:
    for k in range(n-1, 1, -1):
        m = A[k]
        i = 0
        j = k-1
        while i !=j:
            if A[i] + A[j] > m:
                j-=1
            elif A[i] + A[j] < m:
                i+=1
            else:
                count+=1
                # print(f'i, j = {i}, {j}')
                # print(f'm = {m}')
                # print(f'm=')
                break

    print(count)

# 나의 코드 #2: 정답 보고
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
result = 0
for k in range(N):
    find = A[k]
    i = 0
    j = N-1
    while i < j:
        if A[i] + A[j] == find:
            if i == k:
                i+=1
            elif j == k:
                j-=1
            else:
                result +=1
                break
        elif A[i] + A[j] > find:
            j-=1
        else:
            i += 1
print(result)