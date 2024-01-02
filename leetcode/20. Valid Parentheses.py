class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# 24.1.3 수. 복기로 품
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        hm = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in hm.keys():
                stack.append(hm[c])
                # print(stack)
            else:
                if len(stack) !=0 and c == stack[-1] :
                    stack = stack[0:-1]
                    # print(f'stack ={stack}')
                else:
                    return False
        return True if len(stack) == 0 else False

