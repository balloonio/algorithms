class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        result = []
        carried = 0
        last = None
        self.helper(num, 0, carried, last, target, "", result)
        return result

    def helper(self, num, idx, carried, last, target, form, result):
        if idx >= len(num):
            if carried == target:
                result.append(copy.deepcopy(form))
            return

        # edge case
        if last is None:
            if num[idx] == '0':
                self.helper(num, idx+1, 0, 0, target, '0', result)
                return
            size = len(num)
            for end in range(idx, size):
                end += 1
                val = int(num[idx:end])
                form = str(val)
                self.helper(num, end, val, val, target, form, result)
            return

        if num[idx] == '0':
            form += '+0'
            self.helper(num, idx+1, carried, 0, target, form, result)
            form = form[:-2]
            form += '-0'
            self.helper(num, idx+1, carried, 0, target, form, result)
            form = form[:-2]
            form += '*0'
            self.helper(num, idx+1, carried-last, 0, target, form, result)
            form = form[:-2]
            return

        size = len(num)
        for end in range(idx, size):
            end += 1
            val = int(num[idx:end])
            form_size = len(form)
            # plus +
            form += '+' + str(val)
            self.helper(num, end, carried+val, val, target, form, result)
            form = form[:form_size]
            # minus -
            form += '-' + str(val)
            self.helper(num, end, carried-val, -val, target, form, result)
            form = form[:form_size]
            # multiply *
            form += '*' + str(val)
            self.helper(num, end, carried-last+last*val, last*val, target, form, result)
            form = form[:form_size]
        return
