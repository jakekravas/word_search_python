"""
    File: word_search.py
    Author: Jake Kravas
    Purpose: 
    Course: CSC-120
"""

def get_word_list():
    """
        Get user input for word list filename,
        arrange words from file into list
        Returns: list
        Post-condition: Returns a list
    """

    filename = input()
    word_list = []

    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            word_list.append(lines[i].strip())

    return word_list

def get_grid_of_letters():
    """
        Get user input for grid of letters filename,
        arrange letters from file into list of lists
        Returns: list of lists
        Post-condition: Returns a list of lists
    """

    filename = input()
    grid_of_letters = []

    with open(filename) as f:
        lines = f.readlines()

        for i in range(len(lines)):

            line = lines[i].strip()

            # remove all spaces
            line = line.replace(' ', '')

            # turn line from string into list
            line = list(line)

            # prevent empty lines from being appended to list
            if line:
                grid_of_letters.append(line)
        
    return grid_of_letters


def get_grid_strings(grid):
    """
        Get each row, column, and diagonal (top-left to bottom-right)
        from grid in string form and add to lists
        Returns: lists
        Post-condition: Returns several lists
    """

    # lists to string forms of rows/columns from grid
    grid_str_l_r = []
    grid_str_r_l = []
    grid_str_t_b = []
    grid_str_b_t = []
    grid_str_diagonal = ['']
    grid_str_diag = []

    for i in range(len(grid)):

        # string form of row
        row_str_l_r = ''.join(grid[i]).lower()
        # string form of reversed row
        row_str_r_l = ''.join(grid[i]).lower()[::-1]

        grid_str_l_r.append(row_str_l_r)
        grid_str_r_l.append(row_str_r_l)

        # string form of column
        vert_str = ''
        for y in range(len(grid)):
            vert_str += grid[y][i].lower()

        grid_str_t_b.append(vert_str)
        grid_str_b_t.append(vert_str[::-1])


    # get string forms of diagonals from grid
    offset = 0
    while offset < len(grid):

        # temp string for top-left to bottom-right going right
        str_add = ''
        # temp string for top-left to bottom-right going down
        str_add_ = ''

        for i in range(len(grid)):
            
            if i+offset < len(grid[i]):
                # apply offset horizontally
                str_add += grid[i][i + offset].lower()

            if i+offset+1 < len(grid):
                # apply offset vertically
                str_add_ += grid[i+offset+1][i].lower()

        if len(str_add) > 2:
            grid_str_diag.append(str_add)
        if len(str_add_) > 2:
            grid_str_diag.append(str_add_)
        
        offset += 1


    return grid_str_l_r, grid_str_r_l, grid_str_t_b, grid_str_b_t, grid_str_diag


def check_for_matches(word_list, grid_str_list):
    """
        Get word matches
        Returns: list
        Preconditions: word_list is a list, grid_str_list is a list
        Post-condition: Returns list of strings
    """

    matches = []

    for i in range(len(grid_str_list)):
        for y in range(len(word_list)):

            word = word_list[y]
            # if word of at least 2 char is in list, append to matches
            if word in grid_str_list[i] and len(word) > 2:
                matches.append(word)

    return matches


def display_all_matches(matches):
    """
        Display all word matches in alphabetical order
        Preconditions: matches is a list of lists
        Post-condition: Prints all word matches
    """
    all_matches = []
    for i in range(len(matches)):
        if len(matches[i]) > 0:
            for y in range(len(matches[i])):
                all_matches.append(matches[i][y])
    all_matches = sorted(all_matches)
    for i in range(len(all_matches)):
        print(all_matches[i])



def main():
    word_list = get_word_list()
    grid_of_letters = get_grid_of_letters()

    # get string forms of rows/columns/diagonal from grid
    grid_str_l_r, grid_str_r_l, grid_str_t_b, grid_str_b_t, grid_str_diag = get_grid_strings(grid_of_letters)

    # check for word matches in every direction
    l_r_matches = check_for_matches(word_list, grid_str_l_r)
    r_l_matches = check_for_matches(word_list, grid_str_r_l)
    t_b_matches = check_for_matches(word_list, grid_str_t_b)
    b_t_matches = check_for_matches(word_list, grid_str_b_t)
    diagonal_matches = check_for_matches(word_list, grid_str_diag)
    
    # display all word matches
    display_all_matches([l_r_matches, r_l_matches, t_b_matches, b_t_matches, diagonal_matches])

main()
