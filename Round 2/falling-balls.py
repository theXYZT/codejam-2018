# Codejam 2018, Round 2: Falling Balls

def iterate_layout(start, result):
    """Returns next row of layout."""
    row = '.'
    for i in range(1, len(result) - 1):
        if sum(result[:i]) > sum(start[:i]):
            row += '/'
            start[i] -= 1
            start[i - 1] += 1
        elif sum(result[i + 1:]) > sum(start[i + 1:]):
            row += "\\"
            start[i] -= 1
            start[i + 1] += 1
        else:
            row += '.'
    return row + '.'

def make_layout(result):
    """Generate layout that creates result."""
    if result[0] == 0 or result[-1] == 0:
        return None
    start = [1 for _ in range(len(result))]
    layout = []
    while any([a != b for a, b in zip(start, result)]):
        layout.append(iterate_layout(start, result))
    layout.append(len(result) * '.')
    return layout

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_columns = int(input())
    result = tuple([int(i) for i in input().split()])

    layout = make_layout(result)

    if layout is None:
        print("Case #{}: IMPOSSIBLE".format(case))
    else:
        print("Case #{}: {}".format(case, len(layout)))
        for row in layout:
            print("{}".format(row))
