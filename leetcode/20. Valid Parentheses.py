class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = { 'M': 1000, 'CM':900,  'D':500,'CD': 400,    'C': 100, 'XC':90, 'L': 50, 'XL':40, 'X': 10, 'IX': 9,   'IV': 4, 'V': 5,  'III': 3,  'I': 1}
        answer = 0
        for k, v in hashmap.items():
            while True:
                if k == s[:len(k)]:
                    print(f'k= {k}')
                    print(f'v = {v}')
                    answer += v
                    s = s[len(k):]
                    print(f's={s}')
                else:
                    break
        return answer