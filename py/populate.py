import random

def populate(forest, nPop):
    '''
    This function populates the landscape with 'nPop' individuals inside habitat/forest.
    Important: it returns the cell, not the position itself inside the cell!
    Input:
    - forest: cells (row, col) of the map that correspond to habitat/forest.
    - nPop: initial population (number of individuals)
    Output:
    - list of positions (cell) of each individual
    '''
    
    return random.sample(forest, nPop) # no replacement; max one individual per pixel