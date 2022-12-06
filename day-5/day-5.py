def split_starting_layout(input):
    layout = open(input)
    rows = []
    for row in layout:
        rows.append(row)
    print(rows)

    return rows


def determine_grid_size(rows):
    return len(rows[0])


def create_grid_row(row_size):
    grid_row = []
   # grid = []
    for num in range(row_size):
        grid_row.append('_')
    
    return grid_row
    
#    for num in range(size):
#        grid.append(grid_row)

def determine_col_num(row):
    print(type(row))
    #row_nums = row[-1].split()
    #return int(row_nums[-1])


def create_grid(grid_row, col):
    grid = []

    for num in range(col):
        grid.append(grid_row)
    
    print(grid)

rows = split_starting_layout('./starting.txt')
row_len = determine_grid_size(rows)
grid_row = create_grid_row(row_len)
