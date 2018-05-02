class Solution:
    def romanToInt(self, s):
        symbols_integer = {'I':1, 'V':5, 'X':10, 'L':50,
                           'C':100, 'D':500, 'M':1000,
                           'IV':4, 'IX':9, 'XL':40, 'XC':90,
                           'CD':400, 'CM':900}
        length = len(s)
        integer = 0
        isPass = False

        for i in range(length):
            if isPass:
                isPass = False
                continue

            if s[i] in symbols_integer and s[i:i+2] not in symbols_integer:
                integer = integer + symbols_integer[s[i]]
                isPass = False
                continue

            if s[i:i+2] in symbols_integer:
                integer = integer + symbols_integer[s[i:i+2]]
                isPass = True

        return integer

Input = 'DCXXI'

A = Solution()
B = A.romanToInt(Input)
print(B)