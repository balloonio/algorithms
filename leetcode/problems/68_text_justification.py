class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []

        line = []  # words in the current line
        line_chcnt = 0
        result = []

        for word in words:
            if line_chcnt + len(line) + len(word) <= maxWidth:
                line += [word]
                line_chcnt += len(word)
            else:
                # line if full
                modline = self.format_line(line, line_chcnt, maxWidth)
                result += [modline]
                line = [word]
                line_chcnt = len(word)

        # if line has words here, that is the last line that hasnt been formatted yet
        if line:
            modline = self.format_last_line(line, maxWidth)
            result += [modline]
        return result

    def format_last_line(self, line, maxWidth):
        linestr = " ".join(line)
        linestr += " " * (maxWidth - len(linestr))
        return linestr

    def format_line(self, line, chcnt, maxWidth):
        if len(line) == 1:
            return self.format_last_line(line, maxWidth)
        edgecnt = len(line) - 1
        totalsp = maxWidth - chcnt
        minsp = totalsp // edgecnt
        extrasp = totalsp % edgecnt
        linestr = ""
        for edgeidx in range(edgecnt):
            extra = " " if edgeidx < extrasp else ""
            linestr += line[edgeidx] + " " * minsp + extra
        linestr += line[-1]
        return linestr


"""
It is very easy to miss the case where line has only 1 word in format_line
In that case, L40 and L48 will both break, because there is still 1 edge for 1 word
and you dont append the last word again on the line
Therefore, the best way is to just format it the same way as last line 
"""
