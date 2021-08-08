class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            ci = int(s[i])
            cii = int(s[i - 1:i + 1])
            if ci < 1 and cii > 26:
                return 0
            elif ci >= 1 and 10 <= cii <= 26:
                dp[i] = dp[i - 1] + 1
            # 若是10，这里答案是0，可事实上并不是
            # 这里减一的依据是什么？
            elif ci < 1 and cii <= 26:
                dp[i] = dp[i - 1] - 1
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s1 = "06"
    s2 = '226'
    s3 = "12"
    # 1前面要是0，怎么办呢？
    s4 = "2101"
    s5 = "10"
    s6 = "1123"
    sl = [s1, s2, s3, s4, s5]
    for si in sl:
        print(s.numDecodings(si))
