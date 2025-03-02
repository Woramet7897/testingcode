def gridChallenge(grid):
    ordered_grid = [sorted(row) for row in grid]

    for col in range(len(ordered_grid[0])):
        column_values = [ordered_grid[row][col] for row in range(len(ordered_grid))]
        if column_values != sorted(column_values):
            return "NO"

    return "YES"


def check_all(test_cases):
    results = []
    for test_case in test_cases:
        lines = test_case.strip().split("\n")
        if lines[0].isdigit():
            grid = lines[1:]
            results.append(gridChallenge(grid))
    return results
