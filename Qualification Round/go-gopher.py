# Codejam 2018, Qualification: Go, Gopher!

import sys

def make_grid(area):
    """Make orchard grid given required area."""
    height = 3
    width = (area // height) + 1
    return [[1] * width for _ in range(height)]

def prepare_cell(grid, x, y):
    """Prepare cell at x and y."""
    grid[y - 1][x - 1] = 0

def inspect_around_position(grid, x):
    """Inspect cells around position x for preparedness."""
    return sum([sum(row[x-1:x+2]) for row in grid])

def get_next_position(grid):
    """Returns best next position to send."""
    width = len(grid[0])
    unprepared = [inspect_around_position(grid, x) 
                  for x in range(1, width - 1)]

    return unprepared.index(max(unprepared)) + 2

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    area = int(input())
    grid = make_grid(area)

    while True:
        x_send, y_send = get_next_position(grid), 2
        print('{} {}'.format(x_send, y_send), flush=True)

        x_recv, y_recv = [int(i) for i in input().split()]
        if x_recv <= 0 or y_recv <= 0:
            break
        else:
            prepare_cell(grid, x_recv, y_recv)

sys.exit()