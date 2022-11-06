# 책의 풀이


# 나의 풀이
import sys
input = sys.stdin.readline

n, p =  map(int, input().split())
dna = input()
c = list(map(int, input().split()))
std_cnt={'A': c[0], 'C': c[1], 'G': c[2], 'T': c[3]}
i = 0
j =i+p
result = 0

while j <= n :
    temp_dna = dna[i:j]
    dna_cnt = {letter: temp_dna.count(letter) for letter in set(temp_dna)}
    for c in (std_cnt.keys() - dna_cnt.keys()):
        dna_cnt[c] = 0
    if dna_cnt['A'] >= std_cnt['A'] and dna_cnt['C'] >= std_cnt['C'] and dna_cnt['T'] >= std_cnt['T']  and dna_cnt['G'] >= std_cnt['G']:
        result +=1
    i+=1
    j += 1

print(result)



