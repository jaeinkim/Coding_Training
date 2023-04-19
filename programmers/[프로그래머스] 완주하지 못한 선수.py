# 23/2/26 - 1
#   - 정확성 테스트는 맞았으나 효율성 테스트에서 모두 시간 초과 떨어짐

def solution(participant, completion):
    participant_table = dict(zip(participant, [participant.count(key) for key in participant]))

    for name in completion:
        if name in participant_table:
            participant_table[name] -= 1
    for key, value in participant_table.items():
        if value == 1:
            return key

# 23/2/26 - 2
#   - 정확성 테스트는 맞았으나 효율성 테스트에서 모두 시간 초과 떨어짐#

def solution(participant, completion):
    participant_table = {}
    for name in participant:
        if name not in completion:
            return name
        else:
            participant_table[name] = participant_table.get(name, 0) + 1

    for name in completion:
        # if name in participant_table:
        participant_table[name] -= 1
    for key, value in participant_table.items():
        if value == 1:
            return key

# 23/2/26 - 3 (결국 못풀고 정답으로 복기함)
#   - 정확성 테스트는 맞았으나 효율성 테스트에서 모두 시간 초과 떨어짐#
def solution(participant, completion):
    participant_table = {}
    for name in participant:
        if name not in completion:
            return name
        else:
            participant_table[name] = participant_table.get(name, 0) + 1

    for name in completion:
        if name in participant_table:
            participant_table[name] -= 1
    print(participant_table.values())
    print(participant_table.keys())
    hashtable = dict(zip(participant_table.values(), participant_table.keys()))
    print(hashtable)
    return  hashtable[1]

# 정답
def solution(participant, completion):
    table = dict()
    for str in participant:
        if str not in table.keys():
            table[str] =1
        else:
            table[str] += 1
    for str in completion:
        table[str] = table[str] - 1
    for str in table:
        if table[str] ==1:
            return str

# 정답 2
import collections

def solution(participant, completion):
    return list((collections.Counter(participant) - collections.Counter(completion)).keys())[0]





participant= ["leo", "kiki", "eden"]
completion =["eden", "kiki"]
solution(participant, completion)