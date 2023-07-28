def snail(snail_map):
    row = 0
    column = 0
    result = []
    line_len = max(1, len(snail_map) - 1)
    
    if not any(snail_map):
        return []
    
    while True:
        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            for i in range(line_len):
                result.append(snail_map[row][column])

                row += direction[0]
                column += direction[1]

                if len(result) == len(snail_map) ** 2:
                    return result
        row += 1
        column += 1
        line_len = max(1, line_len - 2)