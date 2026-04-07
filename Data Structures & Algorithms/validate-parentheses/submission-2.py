class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para= {')':'(',']':'[','}':'{'}
        for p in s:
            if p in para:
                if not stack or para[p] != stack.pop():
                    return False
            else:
                stack.append(p)  
        return len(stack) == 0