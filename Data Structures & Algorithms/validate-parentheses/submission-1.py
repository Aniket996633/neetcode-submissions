class Solution:
    def isValid(self, s: str) -> bool:
        hash = dict()
        hash[']'] = '['
        hash[')'] = '('
        hash['}'] = '{'
        stack = []
        for char in s:
            if char in hash:
                top_ele = stack.pop() if stack else '#'
                if top_ele != hash[char]:
                    return False

            else:
                stack.append(char)
        return len(stack) == 0