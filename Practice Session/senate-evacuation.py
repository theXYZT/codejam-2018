# Codejam 2018, Practice Session: Senate Evacaution

import string

def evacuate(parties):
    """Evacuates a senator."""
    biggest_party = max(parties, key=parties.get)
    parties[biggest_party] -= 1
    return biggest_party

def next_evacuation_step(parties):
    """Generates the next evacuation step."""
    step = evacuate(parties)
    if sum(parties.values()) != 2:
        step += evacuate(parties)
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
    num_members = map(int, input().split())

    parties = dict(zip(string.ascii_uppercase[:num_parties], num_members))

    plan = make_evacuation_plan(parties)
    print('Case #{}: {}'.format(case, " ".join(plan)))
