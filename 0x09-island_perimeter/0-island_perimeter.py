#!/usr/bin/python3
"""Island perimeter Mock interview"""


def island_perimeter(grid):
    """
    function to calculate the perimter of an Island
    """

    # Base condition to check if grid is empty
    # or first row of grid is empty
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimiter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # check top
                if r == 0 or grid[r - 1][c] == 0:
                    perimiter += 1
                # check bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimiter += 1
                # check left
                if c == 0 or grid[r][c - 1] == 0:
                    perimiter += 1
                # check right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimiter += 1
    return perimiter
