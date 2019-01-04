# Codejam 2018, Round 3: Raise the Roof

from collections import namedtuple
from operator import attrgetter
from math import sqrt

# A column has an index and a vector (x, y, z) referring to its tip
Column = namedtuple("Column", ["id", "x", "y", "z"])

def tilt_angle(a, b):
    """Angle in z-direction for vector from b->a."""
    dx, dy, dz = a.x - b.x, a.y - b.y, a.z - b.z
    return dz / sqrt(dx*dx + dy*dy)

def find_projection(a, b, c):
    """Travel along a->b by the x-y scalar projection of a->b on a->c."""
    abx, aby, abz = b.x - a.x, b.y - a.y, b.z - a.z
    acx, acy, acz = c.x - a.x, c.y - a.y, c.z - a.z
    sp = (abx*acx + aby*acy) / (abx**2 + aby**2)
    return Column(-1, a.x + abx*sp, a.y + aby*sp, a.z + abz*sp)

def get_column_ordering(columns):
    """Finds ordering of columns."""

    # Find tallest column
    tallest = columns.pop(columns.index(max(columns, key=attrgetter("z"))))

    # Find the next column that adds the least tilt
    min_tilt, min_tilt_index = None, None
    for i, column in enumerate(columns):
        tilt = tilt_angle(tallest, column)
        if min_tilt == None or min_tilt > tilt:
            min_tilt, min_tilt_index =  tilt, i
    min_tilt_column = columns.pop(min_tilt_index)

    # Begin reverse order with last two columns
    reverse_order = [tallest, min_tilt_column]

    # Loop through columns finding columns that add the least tilt
    while columns:
        min_tilt, min_tilt_index = None, None
        for i, column in enumerate(columns):
            projection = find_projection(reverse_order[-2], 
                                         reverse_order[-1], column)
            tilt = tilt_angle(projection, column)
            if min_tilt == None or min_tilt > tilt:
                min_tilt, min_tilt_index = tilt, i
        reverse_order.append(columns.pop(min_tilt_index))

    return " ".join([str(column.id) for column in reversed(reverse_order)])


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_columns = int(input())

    # List of columns
    columns = [Column(i+1, *map(int, input().split()))
               for i in range(num_columns)]

    ordering = get_column_ordering(columns)
    print('Case #{}: {}'.format(case, ordering))
