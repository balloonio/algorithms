# 1. Using sorting
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        if not tasks:
            return 0

        if not n:
            return len(tasks)

        task2freq = collections.defaultdict(int)
        for task in tasks:
            task2freq[task] += 1

        ordered_tasks = []
        for task, freq in task2freq.items():
            ordered_tasks.append((-freq, freq, task))
        ordered_tasks.sort()

        task2cool = {}
        workq = []
        while ordered_tasks or task2cool:
            # pick a task from doable tasks, if no then idel
            if not ordered_tasks:
                workq.append("idle")
                task_done = None
            else:
                _, freq, task = ordered_tasks[0]
                ordered_tasks.pop(0)
                workq.append(task)
                task2freq[task] -= 1
                # move to cool down
                task_done = task
                if task2freq[task] > 0:
                    task2cool[task] = n
            # check if cooldown finished
            for task, cool in list(task2cool.items()):
                if task == task_done:
                    continue
                task2cool[task] -= 1
                if task2cool[task] == 0:
                    task2cool.pop(task)
                    ordered_tasks.append((-task2freq[task], task2freq[task], task))
                    ordered_tasks.sort()

        return len(workq)


# 2. Using heapq
class Solution:  # noqa: F811
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        if not tasks:
            return 0

        if not n:
            return len(tasks)

        task2freq = collections.defaultdict(int)
        for task in tasks:
            task2freq[task] += 1

        freq_heapq = []
        for task, freq in task2freq.items():
            freq_heapq.append((-freq, freq, task))
        heapq.heapify(freq_heapq)

        task2cool = {}
        workq = []
        while freq_heapq or task2cool:
            # pick a task from doable tasks, if no then idel
            if not freq_heapq:
                workq.append("idle")
                task_done = None
            else:
                _, freq, task = heapq.heappop(freq_heapq)
                workq.append(task)
                task2freq[task] -= 1
                # move to cool down
                task_done = task
                if task2freq[task] > 0:
                    task2cool[task] = n
            # check if cooldown finished
            for task, cool in list(task2cool.items()):
                if task == task_done:
                    continue
                task2cool[task] -= 1
                if task2cool[task] == 0:
                    task2cool.pop(task)
                    heapq.heappush(
                        freq_heapq, (-task2freq[task], task2freq[task], task)
                    )

        return len(workq)


# 3. (There are faster and more concise solutions which doesn't construct workq)
# I'm not bother to write it here, but those should be around the same time complexity

"""
It is important to realize the key to this question:
to optimize the time, we need to assign slots for all occurance for task with
highest frequency first, and then in between the idle, assign other lower priority
tasks
L42 L43 When decrementing cool down cycles, make sure you are not decrementing
cooldown for the task that we just completed in the current cycle
"""
