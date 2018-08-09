"""

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

"""
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = {}
        ct = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                cnt[ct] = 0
                if grid[m][n] == 1:
                    if m-1 < 0:
                        cnt[ct] += 1
                    else:
                        if grid[m-1][n] == 0:
                            cnt[ct] += 1
                    if m+1 > len(grid) - 1:
                        cnt[ct] += 1
                    else:
                        if grid[m+1][n] == 0:
                            cnt[ct] += 1
                    if n-1 < 0:
                        cnt[ct] += 1
                    else:
                        if grid[m][n-1] == 0:
                            cnt[ct] += 1
                    if n+1 > len(grid[0]) - 1:
                        cnt[ct] += 1
                    else:
                        if grid[m][n+1] == 0:
                            cnt[ct] += 1
                ct += 1
        return sum(cnt.values())
