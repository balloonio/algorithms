class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return "/"
        dir_stack = collections.deque()
        dirs = path.split("/")
        for dir in dirs:
            if not dir or dir == ".":
                continue
            # enter dir
            if dir != "..":
                dir_stack.append(dir)
            # return to upward directory
            elif dir == "..":
                if dir_stack:
                    dir_stack.pop()

        if not dir_stack:
            return "/"
        path = ""
        for dir in dir_stack:
            path += "/" + dir
        return path


# Just need to pay attention to testcases, ask for clarify
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# path = "/a/../../b/../c//.//", => "/c"
# path = "/a//b////c/d//././/..", => "/a/b/c"
# path = "/../", => "/"
