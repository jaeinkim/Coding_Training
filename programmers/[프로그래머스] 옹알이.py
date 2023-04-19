def solution(babbling):
    answer = 0

    std_arr = ['aya', 'ye', 'woo', 'ma']

    for i in range(len(babbling)):
        for std_s in std_arr:
            if babbling[i].startswith(std_s):
                babbling[i] = babbling[i].replace(std_s, '')
    for s in babbling:
        if s == '':
            answer +=1

    return answer

# solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	)
#test2
#test3

# 23/2/26
def solution(babbling):
    std = ['aya', 'ye', 'woo', 'ma']
    count = 0
    for word in babbling:
        for std_word in std:
            if std_word in word:
                # print(word)
                word = word.replace(std_word, '0')
                # print(word)
                count += (1 if word.isdigit() else 0)
    return count