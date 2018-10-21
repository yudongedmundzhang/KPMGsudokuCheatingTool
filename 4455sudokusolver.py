def Test_Four_Or_Five(grid):
    return len(grid)
    


def find_Next_Cell_To_Fill(grid, i, j):
    for x in range(i,Test_Four_Or_Five(grid)):
        for y in range(j,Test_Four_Or_Five(grid)):
            if grid[x][y] == 0:
                return x,y
        for x in range(0,Test_Four_Or_Five(grid)):
            for y in range(0,Test_Four_Or_Five(grid)):
                if grid[x][y] == 0:
                    return x,y
        return -1,-1

def Is_Valid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(Test_Four_Or_Five(grid))])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(Test_Four_Or_Five(grid))])
        if columnOk:
            return True
    return False

def Solve_Sudoku(grid, i=0, j=0):
    i,j = find_Next_Cell_To_Fill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,Test_Four_Or_Five(grid)+1):
        if Is_Valid(grid,i,j,e):
            grid[i][j] = e
            if Solve_Sudoku(grid, i, j):
                return grid
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False