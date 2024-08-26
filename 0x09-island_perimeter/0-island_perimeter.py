#!/usr/bin/python3
"""function returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List of list of integers where 0 represents
    water and 1 represents land.
    :return: Integer representing the perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides of the land cell
                perimeter += 4

                # Check the adjacent cells
                if i > 0 and grid[i-1][j] == 1:  # Up
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # Left
                    perimeter -= 2

    return perimeter
