class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        # 一个符合要求的string他的前面的substring一定也是符合要求的
        # 不可能说一个string str符合要求 结果str[:k]是不符合要求的
        # 于是转化子问题
        # f[i][0] 表示把S[:i+1]变成结尾为0的符合要求的字符串所需的最小flip
        # f[i][0] 表示把S[:i+1]变成结尾为1的符合要求的字符串所需的最小flip
        f = [[math.inf] * 2 for _ in S]
        f[0][0] = 0 if S[0] == "0" else 1
        f[0][1] = 0 if S[0] == "1" else 1

        for i in range(1, len(S)):
            if S[i] == "0":
                f[i][0] = f[i - 1][0]
                f[i][1] = min(f[i - 1][1], f[i - 1][0]) + 1
            else:
                f[i][0] = f[i - 1][0] + 1
                f[i][1] = min(f[i - 1][1], f[i - 1][0])
        return min(f[-1])
