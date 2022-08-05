def dfs(grid, r, c):
    # / 判断 base case
    # / 如果坐标(r, c) 超出了网格范围，直接返回
    if(not inArea(grid, r, c)):
        return
    # / 访问上、下、左、右四个相邻结点

    # /如果这个格子不是陆地或者这个格子是已经被访问过的陆地，则直接返回
    if(grid[r][c] != '1'):
        return
    # / 将当前是陆地的格子标记为「已遍历过」
    grid[r][c] = "2"
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


# / 判断坐标(r, c) 是否在网格中
def inArea(grid, r, c):
    return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])
