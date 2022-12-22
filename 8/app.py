
def driver():
    grid = open("input.txt").readlines()

    # remove \n
    for i in range(len(grid)):
        grid[i] = grid[i].removesuffix('\n')

    # format as 2d array of ints
    for i in range(len(grid)):
        cols = []
        for c in grid[i]:
            cols.append(int(c))
        grid[i] = cols

    total_trees = 0
    visible_trees = [] # list of confirmed visible trees (by tuple of coords), use this to ensure they aren't repeated

    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            # access with grid[row][col]
            # visible from left and right
            visible = [True, True, True, True] # visible on all sides until proven not
            for i in range(0, col): # from left
                if not grid[row][i] < grid[row][col]:
                    visible[0] = False # proven not visible
                    break
            for i in range(col + 1, len(grid[row])): # from right
                if not grid[row][i] < grid[row][col]:
                    visible[1] = False
                    break
            for i in range(0, row): # from top
                if not grid[i][col] < grid[row][col]:
                    visible[2] = False
                    break
            for i in range(row + 1, len(grid)): # from bottom
                if not grid[i][col] < grid[row][col]:
                    visible[3] = False
                    break
            
            for bool in visible:
                if bool:
                    total_trees += 1
                    visible_trees.append((row, col))
                    break

            col += 1
        row += 1

    print(total_trees)

def driver2():
    grid = open("input.txt").readlines()

    # remove \n
    for i in range(len(grid)):
        grid[i] = grid[i].removesuffix('\n')

    # format as 2d array of ints
    for i in range(len(grid)):
        cols = []
        for c in grid[i]:
            cols.append(int(c))
        grid[i] = cols

    greatest_scenic_score = 0

    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            # access with grid[row][col]
            # visible from left and right
            total_scenic_score = 1
            scenic_score = 0
            for i in range(col-1, -1, -1): # to left
                if grid[row][i] >= grid[row][col]:
                    scenic_score += 1
                    break
                else:
                    scenic_score += 1
            total_scenic_score *= scenic_score
            scenic_score = 0
            for i in range(col + 1, len(grid[row])): # to right
                if grid[row][i] >= grid[row][col]:
                    scenic_score += 1
                    break
                else:
                    scenic_score += 1
            total_scenic_score *= scenic_score
            scenic_score = 0
            for i in range(row-1, -1, -1): # to top
                if grid[i][col] >= grid[row][col]:
                    scenic_score += 1
                    break
                else:
                    scenic_score += 1
            total_scenic_score *= scenic_score
            scenic_score = 0
            for i in range(row + 1, len(grid)): # to bottom
                if grid[i][col] >= grid[row][col]:
                    scenic_score += 1
                    break
                else:
                    scenic_score += 1
            total_scenic_score *= scenic_score
            scenic_score = 0

            if total_scenic_score > greatest_scenic_score:
                greatest_scenic_score = total_scenic_score

            col += 1
        row += 1

    print(greatest_scenic_score)


driver2()
