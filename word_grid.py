"""
    File: word_grid.py
    Author: Jake Kravas
    Purpose: Display a grid of randomly generated letters to user,
    with user typing in the size of grid they want
    Course: CSC-120
"""
from random import *
import string

def init():
    """
        Get grid size input from user, get seed value from user,
        generate seed, and return grid size
        Preconditions: grid is a list of lists,
        0 ≤ n < length of shortest grid row
        Post-condition: The return value is an integer
    """
    grid_size = int(input())
    seed_value = input()
    seed(seed_value)
    return grid_size

def make_grid(grid_size):
    """
        Create grid (list of lists) consisting of random letters
        using grid_size argument as the list size
        Preconditions: grid_list is an integer
        Post-condition: The return value is a list of lists
    """

    grid = []

    for i in range(grid_size):

        rows = []

        for y in range(grid_size):
            # random number from 0-25
            random_num = randint(0,25)
            # letter based on on random_num
            letter = string.ascii_lowercase[random_num]
            rows.append(letter)

        grid.append(rows)
    
    return grid


def print_grid(grid):
    """
        Display each row of grid with just a comma separating each letter
        Preconditions: grid is a list of lists
        Post-condition: Each row of grid is printed
        as a string with a comma separating each letter
    """
    for i in range(len(grid)):
        # get string form of grid row, each element separated by a comma
        grid_row_str = ','.join(grid[i])
        print(grid_row_str)

def main():
    # get grid size from user
    grid_size = init()
    # create grid
    grid = make_grid(grid_size)
    # display grid
    print_grid(grid)

main()
