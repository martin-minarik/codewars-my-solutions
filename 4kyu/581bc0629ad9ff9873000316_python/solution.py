import re
from operator import add, mul, sub, truediv

operations = (truediv, mul, sub, add)


def calculate(expression):
    try:
        parts = re.findall(r"\d+(?:\.\d+)?|[+*$-](?=\d)", expression)
        if sum(map(len, parts)) != len(expression):
            raise ValueError

        for op_idx, op in enumerate("$*-+"):
            while True:
                try:
                    idx = parts.index(op)
                except ValueError:
                    break
                else:
                    right = float(parts.pop(idx + 1))
                    parts.pop(idx)
                    left = float(parts.pop(idx - 1))
                    parts.insert(idx - 1, operations[op_idx](left, right))

        result = float(parts[0])

    except ValueError:
        return "400: Bad request"
    else:
        return int(result) if result == int(result) else result