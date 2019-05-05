# Codejam 2018, Round 1C: Ant Stack

def get_max_stack(ant_list):
    """Get size of largest possible ant stack."""
    stacks = [0,]

    # 0/1 Knapsack Problem
    for ant in ant_list:
        temp_stacks = stacks[:]

        for i in range(len(stacks)):
            if stacks[i] <= 6 * ant:
                if i == len(stacks) - 1:
                    temp_stacks.append(stacks[i] + ant)
                elif stacks[i + 1] > stacks[i] + ant:
                    temp_stacks[i + 1] = stacks[i] + ant
        stacks = temp_stacks

    return len(stacks) - 1

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_ants = int(input())
    ant_list = tuple(int(i) for i in input().split())
    max_stack = get_max_stack(ant_list)
    print('Case #{}: {}'.format(case, max_stack))
