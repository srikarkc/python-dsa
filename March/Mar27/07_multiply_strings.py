class Solution:
    def multiplyStrings(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                pos1 = i + j
                pos2 = i + j + 1

                total = mul + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str or "0"