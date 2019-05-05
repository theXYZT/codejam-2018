# Codejam 2018, Qualification Round: Trouble Sort

def interleave(a, b):
    """Interleave two lists."""
    c = a + b
    c[::2] = a
    c[1::2] = b
    return c

def trouble_sort(number_list):
    """Efficiently compute trouble sort."""
    slice_a = sorted(number_list[::2])
    slice_b = sorted(number_list[1::2])
    return interleave(slice_a, slice_b)

def is_sorted(number_list):
    """Returns index of first sorting failure if not sorted."""
    for i in range(len(number_list) - 1):
        if number_list[i] > number_list[i+1]:
            return i
    return None

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    number_list = [int(i) for i in input().split()]

    trouble_sorted = trouble_sort(number_list)
    sort_check = is_sorted(trouble_sorted)

    if sort_check is None:
        print('Case #{}: OK'.format(case))
    else:
        print('Case #{}: {}'.format(case, sort_check))
