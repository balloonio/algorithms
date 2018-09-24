# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def __init__(self):
        self.cache_size = 0
        self.cache_buf = [""] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # n smaller than cache size, not need to call read4
        if n <= self.cache_size:
            self.copy_size(buf, self.cache_buf, n)
            self.cache_buf = self.cache_buf[n:] + self.cache_buf[:n]
            self.cache_size -= n
            return n

        # need all cache, and call read4
        n -= self.cache_size
        start = self.cache_size
        self.copy_size(buf, self.cache_buf, self.cache_size)
        self.cache_size = 0

        mult4read = n / 4
        remain4read = n % 4

        for i in range(mult4read):
            self.cache_size = read4(self.cache_buf)
            if not self.cache_size:
                return start
            self.copy_size(buf, self.cache_buf, self.cache_size, start)
            start += self.cache_size
            self.cache_size = 0

        self.cache_size = read4(self.cache_buf)
        read_size = min(remain4read, self.cache_size)
        self.copy_size(buf, self.cache_buf, read_size, start)
        self.cache_buf = self.cache_buf[read_size:] + self.cache_buf[:read_size]
        start += read_size
        self.cache_size -= read_size
        return start

    def copy_size(self, des, src, n, start=0):
        for i in range(n):
            des[i + start] = src[i]
