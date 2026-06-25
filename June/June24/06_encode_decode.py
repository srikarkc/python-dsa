class Solution:

    def encode(self, strs):
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s):

        i = 0
        result = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(str(s[i:j]))
            i = j

        return result
