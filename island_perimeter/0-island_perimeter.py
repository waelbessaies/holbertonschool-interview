#!/usr/bin/python3
""" 0-island_perimeter module """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """

    perimeter = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    α, β = i + x, j + y
                    if α >= m or β >= n or α < 0 or β < 0 or grid[α][β] == 0:
                        perimeter += 1

    return perimeter
