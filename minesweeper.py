"""
Return an output grid of mines / count of adjacent cells with mines.

Take an input_grid that represents spaces with or without mines, and
return an output grid of the same dimensions with the following values:
* A "#" value where the input_grid has a "#" value (represents a mine)
-or-
* A count of adjacent cells that hold mines (where input_grid has "-")

The input_grid is a 2D list; the program loops through each column
within each row, and calls a dedicated function to calculate the number
of adjacent cells with mines (horizontally, vertically, and diagonally).
"""

input_grid = [  ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"]   ]


def adjacent_positions(row, col):
    """ A function to determine the value for each mine-free cell. """
    mine_count = 0

    # Determine the start and end ROW number to search for mines in.
    if row != 0:
        start_row = row-1
    else:
        start_row = row

    if row != len(input_grid)-1:
        end_row = row+1
    else:
        end_row = row

    # Determine the start and end COLUMN number to search for mines in.
    if col != 0:
        start_col = col-1
    else:
        start_col = col

    if col != len(input_grid[0])-1:
        end_col = col+1
    else:
        end_col = col

    # Loop through the input_grid from the start column/row.
    for i in range(start_row, end_row+1):
        for j in range(start_col, end_col+1):
            if input_grid[i][j] == "#":
                mine_count += 1

    # Return the final count of mines.
    return mine_count


output_grid = []

# Loop through the input grid.
# Write "#" to the current row for the output grid for a mine.
# Otherwise, call the function to calculate the mine count for "-".

for row in enumerate(input_grid):
    output_row = []
    
    for col in enumerate(row[1]):
        if col[1] == "#":
            output_row.append(col[1])
        else:
            output_row.append(str(adjacent_positions(row[0], col[0])))
    
    output_grid.append(output_row)

# Print the output_grid, one row at a time.
for i in output_grid:
    print(i)