# Codejam 2018, Round 1B: Transmutation

def can_make_metal(i, amount, treasury, formulas):
    """Returns True if we can make amount of metal i."""
    if treasury[i] >= amount:
        treasury[i] -= amount
        return True
    elif treasury[i] >= 0:
        treasury[i] -= amount
        extra = -treasury[i]
        metal_1, metal_2 = formulas[i]

        result = (can_make_metal(metal_1, extra, treasury, formulas) and 
                  can_make_metal(metal_2, extra, treasury, formulas))
        if result:
            treasury[i] += extra

        return result
    else:
        return False

def binary_search(treasury, formulas):
    """Runs binary search to find maximum amount of lead possible."""
    min_lead = treasury[0]
    max_lead = min_lead + sum(treasury[1:]) // 2

    while max_lead > min_lead:
        test_lead = (max_lead + min_lead + 1) // 2

        if can_make_metal(0, test_lead, treasury[:], formulas[:]):
            min_lead = test_lead
        else:
            max_lead = test_lead - 1

    return min_lead

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_metals = int(input())

    formulas = tuple(tuple(int(i) - 1 for i in input().split())
                     for _ in range(num_metals))
    treasury = [int(i) for i in input().split()]

    max_lead = binary_search(treasury, formulas)
    print("Case #{}: {}".format(case, max_lead))
