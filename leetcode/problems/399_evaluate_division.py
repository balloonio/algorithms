class Solution:
    def __init__(self):
        self.var2unit = {}  # to base unit
        self.var2mult = {}  # to multiplier

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        if not queries:
            return []

        for i, eq in enumerate(equations):
            first, second = eq
            if first not in self.var2unit and second not in self.var2unit:
                self.var2unit[first] = second
                self.var2mult[first] = values[i]
                self.var2unit[second] = second
                self.var2mult[second] = 1
            elif first in self.var2unit and second in self.var2unit:
                self.base_unit_conversion(first, second, values[i])
            elif first in self.var2unit:
                multiplier, unit = self.evaluate(first)
                self.var2mult[second] = multiplier / values[i]
                self.var2unit[second] = unit
            else:
                multiplier, unit = self.evaluate(second)
                self.var2mult[first] = multiplier * values[i]
                self.var2unit[first] = unit
        result = []
        for query in queries:
            first, second = query
            first_mult, first_unit = self.evaluate(first)
            second_mult, second_unit = self.evaluate(second)

            if first_unit == "?" or second_unit == "?" or first_unit != second_unit:
                result += [-1.0]
            else:
                result += [first_mult / second_mult]
        return result

    def base_unit_conversion(self, first, second, ratio):
        first_mult, first_unit = self.evaluate(first)
        second_mult, second_unit = self.evaluate(second)
        if first_unit == second_unit:
            return
        # 1st multi * 1st unit / (2nd multi * 2nd unit) = ratio
        # => 1st unit = ratio * 2st mult / 1nd multi in terms of 2nd unit
        self.var2unit[first_unit] = second_unit
        self.var2mult[first_unit] = ratio * second_mult / first_mult
        return

    def evaluate(self, unit):
        if unit not in self.var2unit:
            return -1.0, "?"
        multiplier = 1
        while unit != self.var2unit[unit]:
            multiplier *= self.var2mult[unit]
            unit = self.var2unit[unit]
        return multiplier, unit


"""
union find
base_unit_conversion is like union
evaluate is like find
"""
