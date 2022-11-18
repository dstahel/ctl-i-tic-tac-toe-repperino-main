import numpy as np
import sys
import os.path
import os


def startgame(filepath, size):
    try:
        array = np.loadtxt(filepath)
        grid = array.astype(int)
    except:
        array = np.zeros((size, size))
        grid = array.astype(int)
    return grid
# if any value isn't either 0,1,2 grid is not legal
# if difference in plays is > 1 grid is not legal
def legal(grid):
    diff = np.count_nonzero(grid == 1) - np.count_nonzero(grid == 2)
    if np.any(grid < 0)== True or np.any(grid > 2 )== True  or diff > 1 or diff< 0:
        return False


# check for winner
def winner(grid):
    for i in range(len(grid)):
        if np.all(grid[i]== 1) == True or np.all(grid[:,i]== 1)== True:
            return 1
        if np.all(grid[i]== 2) == True or np.all(grid[:,i]== 2)== True:
            return 2
    if np.all(grid.diagonal() == 1)== True or np.all(np.fliplr(grid).diagonal()== 1)== True:
        return 1
    if np.all(grid.diagonal() == 2)== True or np.all(np.fliplr(grid).diagonal()== 2)== True:
        return 2
    else:
        return 0


if os.path.isfile("tic-tac-toe.txt"):
  os.remove("tic-tac-toe.txt")
