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
#test