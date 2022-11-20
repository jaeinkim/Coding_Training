# 나의 풀이
def solution(my_string):
    return ''.join([ch for ch in my_string if ch not in ['a', 'e', 'i', 'o', 'u']])

# 다른 사람 풀이
def solution(my_string):
    for ch in 'aeiou':
        my_string = my_string.replace(ch, '')
    return my_string