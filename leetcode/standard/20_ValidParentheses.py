class Solution(object):
    def isValid(self, s):
        n = len(s)

        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()','').replace('[]','')

        if s == '':
            return True
        else:
            return False

    def isValid1(self, s):
        stack = []
        dict = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

Input = "[][]"
A = Solution()
B = A.isValid1(Input)
print(B)
