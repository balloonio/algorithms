class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0

        heights.append(0)
        # mono increasing stack
        mono_stack = collections.deque()
        result = 0
        for i, height in enumerate(heights):
            # try to push to mono stack, pop top until we can push
            last_popped = None
            while mono_stack and heights[mono_stack[-1]] >= height:
                last_popped = mono_stack.pop()
                before_popped = mono_stack[-1] if mono_stack else None

                # calculte area for the pilar at the index just being popped
                # i = the first index on right with height smaller than heights[last_popped]
                # before_popped = the last index on left with height smaller than heights[last_popped]
                area = 0
                area += heights[last_popped] * (i - last_popped)
                area += heights[last_popped] * (
                    last_popped - before_popped - 1
                    if before_popped is not None
                    else last_popped
                )
                result = max(result, area)

            mono_stack.append(i)

        return result
