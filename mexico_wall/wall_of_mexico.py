"""
function `find_min_wall_length` solves part 1(a) of the question.

funtion `breadth_first_search` is the answer to the second part.
"""


def is_valid_cell(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    return i < rows and i >= 0 and j < cols and j >= 0


def find_min_wall_length(matrix, i, j, threshold):
    directions = [(0,1), (1,0), (-1, 0), (0, -1)]
    cost = 0
    res = threshold

    queue = []

    queue.append((i, j, cost))
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    existing_costs = [[float('inf')] * len(matrix[0])
                       for _ in range(len(matrix))]

    while queue:

        i, j, csf = queue.pop(0)

        # Pruning: if cost so far exceeds the min path found already
        # no need to explore further
        if csf > res:
            continue

        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if is_valid_cell(matrix, new_i, new_j) and not visited[new_i][new_j]:
                cell_val = matrix[new_i][new_j]
                if cell_val == "A":
                    # Atlantic is reached, yay!
                    res = min(res, csf)
                    continue
                elif cell_val == "." or cell_val == "M" or cell_val == "U" or cell_val == "P":
                    # no path possible
                    visited[new_i][new_j] = True
                    continue
                else:
                    # it's a digit
                    if existing_costs[new_i][new_j] > csf + int(cell_val):
                        queue.append((new_i, new_j, csf + int(cell_val)))
                        existing_costs[new_i][new_j] = csf + int(cell_val)
    return res


def breadth_first_search(matrix, i, j):
    directions = [(0,1), (1,0), (-1, 0), (0, -1)]
    cost = 0
    res = float('inf')

    queue = []

    queue.append((i, j, cost))
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    while queue:

        i, j, csf = queue.pop(0)

        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if is_valid_cell(matrix, new_i, new_j) and not visited[new_i][new_j]:
                cell_val = matrix[new_i][new_j]
                visited[new_i][new_j] = True
                if cell_val == "A":
                    # Atlantic is reached, yay!
                    # since this all the paths have equal cost and we're using
                    # breadth first search, this is certainly shortest path.
                    # So.. return!
                    return csf
                elif cell_val == "." or cell_val == "M" or cell_val == "U" or cell_val == "P":
                    # no path possible
                    continue
                else:
                    # it's a digit
                    queue.append((new_i, new_j, csf + int(cell_val)))
    return res


# row, col, inputs
test_case_1 = (4, 5, """. U U U
P 1 1 3 A
P 3 1 1 A
. M M M""")

test_case_2 = (11, 15, """. U U U U U U
P 7 9 8 8 7 5 U . . . U U U
P 2 2 2 1 1 6 6 U U U 5 5 U A
P 1 2 3 2 2 2 2 4 5 5 4 2 5 A
. M M M 3 3 3 2 6 5 4 2 2 2 A
. . . . M M 2 2 2 2 3 7 2 2 A
. . . . . . M 2 3 2 7 7 7 7 A
. . . . . . . M 7 7 7 7 7 7 A
. . . . . . . M 7 7 7 M M 7 A
. . . . . . . . M 7 M
. . . . . . . . . M""")

test_cases = [test_case_1, test_case_2]


for test_case in test_cases:
    num_rows, num_cols = test_case[0], test_case[1]
    lines = test_case[2].split('\n')

    matrix = []

    for line in lines:
        cells = line.split()
        cell_len = len(cells)
        cells += ["."] * (num_cols - cell_len)
        matrix.append(cells)

    # min cost path so far
    mcpsf = float('inf')

    print(matrix)

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if matrix[row_idx][col_idx] == 'P':
                mcpsf = min(mcpsf, find_min_wall_length(
                    matrix, row_idx, col_idx, mcpsf))

    print("Minimum cost is: {}".format(mcpsf))
