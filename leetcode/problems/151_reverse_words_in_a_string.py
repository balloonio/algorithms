class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        curr_word = None
        stack = collections.deque()

        for c in s:
            if c == " " and curr_word is not None:
                stack.append(curr_word)
                curr_word = None
            elif c != " ":
                if curr_word is None:
                    curr_word = c
                else:
                    curr_word += c
        if curr_word:
            stack.append(curr_word)
        result = ""
        while stack:
            if result != "":
                result += " "
            result += stack.pop()
        return result


"""
注意L22和L23不要忘记, 这个好像是一个经常犯的错误,根据空格来push一些东西
但是句尾是没有空格的 有可能最后一个词没有被push
"""
