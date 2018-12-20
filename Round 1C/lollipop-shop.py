# Codejam 2018, Round 1C: Lollipop Shop

import sys

def find_best_flavor(preferences, flavor_data):
    """Returns best flavor to give customer."""
    for preference in preferences:
        if preference in flavor_data:
            flavor_data[preference] += 1

    flavor_subset = {k: flavor_data[k] for k in preferences
                     if k in flavor_data}

    if len(flavor_subset) > 0:
        chosen_flavor = min(flavor_subset, key=flavor_subset.get)
        _ = flavor_data.pop(chosen_flavor)
    else:
        chosen_flavor = -1

    return chosen_flavor 

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    flavor_data = dict([(i, 0) for i in range(N)])

    for i in range(N):
        D, *preferences = [int(i) for i in input().split()]

        if D > 0:
            flavor = find_best_flavor(preferences, flavor_data)
            print('{}'.format(flavor), flush=True)
        else:
            print('{}'.format(-1), flush=True)

sys.exit()
