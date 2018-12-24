# Codejam 2018, Round 1B: Mysterious Road Signs

from collections import namedtuple

Sign = namedtuple("Sign", ["M", "N"])

def largest_valid_sets(signs):
    """Returns size of largest valid set, and number of such sets."""
    len_set, num_set = 1, 1

    # Make two passes over data tracking changes in M and N
    # i_set =  Starting index of current valid set
    # i_next = Starting index of next valid set
    Mpass = {'M': signs[0].M, 'N': signs[0].N, 'i_next': 0, 'i_set': 0}
    Npass = {'M': signs[0].M, 'N': signs[0].N, 'i_next': 0, 'i_set': 0}

    for i_sign, sign in enumerate(signs[1:], start=1):
        temp_Mpass, temp_Npass = dict(Mpass), dict(Npass)

        # Check changes in M
        if sign.M == temp_Mpass['M']:
            Mpass = dict(temp_Mpass)
        else:
            Mpass = dict(temp_Npass)
            if sign.M != Mpass['M']:
                Mpass['M'] = sign.M
                Mpass['i_set'] = Mpass['i_next']
            Mpass['i_next'] = i_sign

        # Check changes in N
        if sign.N == temp_Npass['N']:
            Npass = dict(temp_Npass)
        else:
            Npass = dict(temp_Mpass)
            if sign.N != Npass['N']:
                Npass['N'] = sign.N
                Npass['i_set'] = Npass['i_next']
            Npass['i_next'] = i_sign

        # There can only be one unique largest valid set at any index
        curr_set = max(i_sign - Mpass['i_set'] + 1,
                       i_sign - Npass['i_set'] + 1)

        if curr_set > len_set:
            len_set, num_set = curr_set, 1
        elif curr_set == len_set:
            num_set += 1

    return len_set, num_set

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_signs = int(input())

    signs = []
    for _ in range(num_signs):
        D, A, B = [int(i) for i in input().split()]
        signs.append(Sign(D + A, D - B))

    set_size, num_sets = largest_valid_sets(signs)
    print("Case #{}: {} {}".format(case, set_size, num_sets))
