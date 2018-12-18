# Codejam 2018, Practice Session: Senate Evacaution

import string

def next_evacuation_step(parties):
    """Generates the next evacuation step."""
    biggest_party = max(parties, key=parties.get)
    step = biggest_party
    parties[biggest_party] -= 1
    if sum(parties.values()) != 2:
        biggest_party = max(parties, key=parties.get)
        parties[biggest_party] -= 1
        step += biggest_party
    return step

def make_evacuation_plan(parties):
    """Generates full evacuation plan."""
    plan = []
    while sum(parties.values()) > 0:
        plan.append(next_evacuation_step(parties))
    return plan

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_parties = int(input())
    num_members = [int(i) for i in input().split()]

    parties = dict(zip(string.ascii_uppercase[:num_parties], num_members))

    plan = make_evacuation_plan(parties)
    print('Case #{}: {}'.format(case, " ".join(plan)))
