# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if not n:
            return 0
        del buf[:]
        read = [""] * 4
        total_read_size = 0
        for i in range(n // 4):
            read_size = read4(read)
            buf += read
            total_read_size += read_size
            if read_size == 0:
                break
        if n % 4:
            read_size = read4(read)
            buf += read[: min(read_size, n % 4)]
            total_read_size += min(read_size, n % 4)

        return total_read_size
