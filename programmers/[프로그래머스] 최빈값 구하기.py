# 나의 풀이
def solution(array):
    answer = 0
    set_array = set(array)
    count_dict = {}
    for num in set_array:
        idx = array.count(num)
        # print(f'{num} {idx}')
        if count_dict.get(idx) is None:
            count_dict[idx] = [num]
        else:
            count_dict[idx] = [num] +count_dict[idx]
    # print(max(count_dict))
    max_count_nums = count_dict[max(count_dict)]
    return -1 if len(max_count_nums) >=2 else max_count_nums[0]

print(solution([1, 2, 3, 3, 3, 4]))