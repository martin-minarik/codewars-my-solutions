import re
from operator import add, mul, sub, truediv


class Calculator:
    operators = {'/': truediv, '*': mul, '-': sub, '+': add}

    @classmethod
    def _evaluate(cls, expression):
        parts = expression.split()
        for op, operation in cls.operators.items():
            idx = 0
            while True:
                try:
                    idx = parts[idx:].index(op) + idx
                except ValueError:
                    break
                else:
                    right = float(parts.pop(idx + 1))
                    parts.pop(idx)
                    left = float(parts.pop(idx - 1))
                    parts.insert(idx - 1, str(operation(left, right)))
                    print(" ".join(parts))
        return str(parts[0])

    @classmethod
    def solve_parentheses(cls, expression):
        pattern = re.compile(r"\(((?:\d+(?:\.\d+)?|[\s*/+-])+)\)")
        sub_parantheses = lambda match: cls._evaluate(match.group(1))
        while True:
            new = pattern.sub(sub_parantheses, expression)
            if new == expression:
                break
            expression = new
        return new

    @classmethod
    def evaluate(cls, expression):
        expression = cls.solve_parentheses(expression)
        result = float(cls._evaluate(expression))

        return int(result) if result == int(result) else result