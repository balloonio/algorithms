class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name and not typed:
            return True
        if not name or not typed:
            return False

        # f[i][j] = typed[:j] can match to name[:i] or not
        nlen, tlen = len(name), len(typed)

        if nlen == tlen:
            return name == typed

        f = [[False] * (tlen + 1) for _ in range(nlen + 1)]
        f[0][0] = True

        for i in range(nlen + 1):
            for j in range(tlen + 1):
                if i == 0 and j == 0:
                    continue
                f[i][j] = False
                # normal type - name[i] == type[j] and f[i-1][j-1] is true
                f[i][j] |= (
                    True
                    if (
                        name[i - 1] == typed[j - 1]
                        and i - 1 >= 0
                        and j - 1 >= 0
                        and f[i - 1][j - 1]
                    )
                    else False
                )
                # long press - type[j] == type[j-1] and f[i]f[j-1] is true
                f[i][j] |= (
                    True
                    if (
                        typed[j - 1] == typed[j - 2]
                        and j - 1 >= 0
                        and j - 2 >= 0
                        and f[i][j - 1]
                    )
                    else False
                )

        return f[-1][-1]


"""
太久没有写序列型dp了 居然出了严重silly的bug
L22 L23这里居然忘记 +1 了, 导致最后一排dp直接没有算...
        for i in range(nlen + 1):
            for j in range(tlen + 1):
同样的原因导致在compare character的时候也忘记 -1 了... 导致程序完全错..
name[i - 1] == typed[j - 1]

还有一个地方是这里, 如果不写的话会超时, 注意算dp之前先看一下是不是可以直接线性处理掉
        if nlen == tlen:
            return name == typed
"""
