class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ## Recursively binary add.
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

    def addBinary1(self, a, b):
        #iteratively
        carry_in, index = '0', 0
        result = ''

        while index < max(len(a), len(b)) or carry_in == '1':
            num_a = a[-1-index] if index < len(a) else '0'
            num_b = b[-1-index] if index < len(b) else '0'

            val = int(num_a) + int(num_b) + int(carry_in)
            result += str(val % 2)
            carry_in = '1' if val > 1 else '0'
            index += 1
        return  result

    def addBinary2(self, a,b):
        def addBinary(self, a, b):
            return bin(eval("0b" + a) + eval("0b" + b))[2:]


a = '1010'
b = '1011'

A = Solution()
B = A.addBinary(a, b)

print(B)