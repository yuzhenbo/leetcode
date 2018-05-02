class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        common_prefix = strs[0]
        for string in strs:
            min_len = min(len(string), len(common_prefix))
            mark = 0
            for i in range(min_len):
                mark = i
                if string[i] == common_prefix[i]:
                    i += 1
                    mark = i
                else:
                    if i == 0:
                        return ''
                    break
            common_prefix = common_prefix[:mark]

        return common_prefix

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ''
        for i, letter_group in enumerate(zip(*strs)):
            #判断前缀是否都一样，如果不一样则返回
            if len(set(letter_group)) > 1:
                return strs[0][:1]
            #如果不一样则用min弄出来，我们可以换一个方式弄出来，见２
        else:
            return min(strs)

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ''
        l = 0
        for cg in zip(*strs):
            if len(set(cg)) > 1:
                return strs[0][:1]
            l += 1
        return strs[0][:l]
Input = ["abc", "abc", "abc","abc"]

A = Solution()
B = A.longestCommonPrefix2(Input)
print(B)