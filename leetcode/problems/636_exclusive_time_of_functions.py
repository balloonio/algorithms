class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return []

        runtime = [0] * n
        func_stack = collections.deque()  # [ (fid, start/unpause time) ]

        for log in logs:
            fid, op, time = self.parse_log(log)

            if op == "start":
                # calculate curr function if any before start this function
                if func_stack:
                    last_fid, last_start = func_stack[-1]
                    runtime[last_fid] += time - last_start
                # push this function
                func_stack.append([fid, time])
            else:
                # calculate this function before return, fid must equal to last_fid here
                last_fid, last_start = func_stack.pop()
                runtime[last_fid] += time - last_start + 1
                # if there is any previous function running, unpause
                if func_stack:
                    func_stack[-1][1] = time + 1
        return runtime

    def parse_log(self, log):
        if not log:
            return None, None, None

        fid, op, time = log.split(":")
        fid, time = int(fid), int(time)
        return fid, op, time


"""
consider a function as pause when a new function starts on top
and unpause when the functions on top of it returns
"""
