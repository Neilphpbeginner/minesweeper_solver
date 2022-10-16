example = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]


def solve_minesweeper(grid):

    def in_parameters(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            counter = 0
            if grid[i][j] == "-":
                if in_parameters(i, j + 1) and grid[i][j + 1] == "#":
                    counter += 1
                if in_parameters(i + 1, j) and grid[i + 1][j] == "#":
                    counter += 1
                if in_parameters(i + 1, j + 1) and grid[i + 1][j + 1] == "#":
                    counter += 1
                if in_parameters(i - 1, j - 1) and grid[i - 1][j - 1] == "#":
                    counter += 1
                if in_parameters(i - 1, j) and grid[i - 1][j] == "#":
                    counter += 1
                if in_parameters(i, j - 1) and grid[i][j - 1] == "#":
                    counter += 1
                if in_parameters(i + 1, j - 1) and grid[i + 1][j - 1] == "#":
                    counter += 1
                if in_parameters(i - 1, j + 1) and grid[i - 1][j + 1] == "#":
                    counter += 1
                grid[i][j] = counter
    return grid


test = solve_minesweeper(example)

for i in test:
    print(i)
