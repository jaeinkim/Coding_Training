#1. 개선 전 코드: grid를 계속 넣어야 하는 점이 불편
class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i>=len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

#2. 개선 후 코드(1): 클래스 변수 이용 / self가 중복
class Solution:
    grid: List[List[str]]

    def dfs(self, i, j):
        if i < 0 or i>=len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] == '0':
            return

        self.grid[i][j] = '0'

        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j)
        return count

#3. 개선 후 코드(2): 중복함수 이용
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i>=len([grid]) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count