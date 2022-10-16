
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


    # return participant[0]



participant= ["leo", "kiki", "eden"]
completion =["eden", "kiki"]
solution(participant, completion)