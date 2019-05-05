# Codejam 2018, Qualification Round: Trouble Sort

import itertools

def trouble_sort(num_list):
    """Efficiently compute trouble sort."""
    a, b = sorted(num_list[::2]), sorted(num_list[1::2])
    c = list(itertools.chain(*itertools.zip_longest(a, b)))
    if c[-1] is None:
        c.pop()
    return c

def is_sorted(num_list):
    """Returns index of first sorting failure if not sorted."""
    for i, (a, b) in enumerate(zip(num_list, num_list[1:])):
        if a > b:
            return i
    return 'OK'

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    number_list = list(map(int, input().split()))

    trouble_sorted = trouble_sort(number_list)
    sort_check = is_sorted(trouble_sorted)
    print('Case #{}: {}'.format(case, sort_check))
