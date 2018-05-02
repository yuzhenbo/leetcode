class Solution:
    def isValid(self, s):
        parenthes_stack = []
        match_rule = {')':'(', ']':'[', '}':'{'}

        for symble in s:
            if symble == '(' or symble == '[' or symble == '{':
                parenthes_stack.append(symble)
            else:
                if (parenthes_stack and parenthes_stack[-1] == match_rule[symble]):
                    parenthes_stack.pop()
                else:
                    return False

        if parenthes_stack:
            return False

        return True

Input = "[][]{"
A = Solution()
B = A.isValid(Input)
print(B)

