import math
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = collections.deque()
        OP = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in OP:
                stack.append( int(t) )
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append( l + r )
                    print(l, " + ", r, " = ", stack[-1])
                elif t == "-":
                    stack.append( l - r )
                    print(l, " - ", r, " = ", stack[-1])
                elif t == "*":
                    stack.append( l * r )
                    print(l, " * ", r, " = ", stack[-1])
                elif t == "/":
                    result = l / r
                    result = math.floor(result) if result >= 0 else math.ceil(result)
                    stack.append( result )
                    print(l, " // ", r, " = ", stack[-1])
        return stack[-1]

# Pay attention to L25 L26 integer division when it is not perfectly divisible and result is negative