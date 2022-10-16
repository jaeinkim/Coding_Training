#책의 코드
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:  # 정답 케이스
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)





# 나의 코드
n  = int(input())
start_index = 1
end_index = 1
sum = 1
count = 1

while end_index != n:
    if n == sum:
        end_index += 1
        sum += end_index
        count += 1
    elif n > sum:
        end_index+=1
        sum += end_index
    else:
        sum -= start_index
        start_index += 1
print(count)