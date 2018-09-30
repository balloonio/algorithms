class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        pre2next = collections.defaultdict(set)

        for (next, pre) in prerequisites:
            indegree[next] += 1
            pre2next[pre].add(next)

        q = collections.deque()
        for course, degree in enumerate(indegree):
            if not degree:
                q.append(course)
        seq = []
        while q:
            course = q.popleft()
            seq += [course]
            for next in pre2next[course]:
                indegree[next] -= 1
                if not indegree[next]:
                    q.append(next)

        if len(seq) != numCourses:
            return []
        return seq
