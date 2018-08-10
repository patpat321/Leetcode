"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    cnt += 1
        return cnt
    
    def dfs(self, i, j, grid):
        stack = [[i,j]]
        while stack:
            i, j = stack.pop()
            if grid[i][j] == "0":              
                continue
            else:
                grid[i][j] = "0"
            if i > 0:
                stack.append([i-1, j])
            if i < len(grid)-1:
                stack.append([i+1, j])
            if j > 0:
                stack.append([i, j-1])
            if j < len(grid[0])-1:
                stack.append([i, j+1])
 """
 Use simple dfs/bfs to search and mark each island.
 """
