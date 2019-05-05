# Codejam 2018, Qualification Round: Saving the Universe Again

def calculate_damage(program):
    """Calculate the damage done by program."""
    strength, damage = 1, 0
    for instruction in program:
        if instruction == 'C':
            strength *= 2
        else:
            damage += strength
    return damage

def hack_once(program):
    """Hack program once."""
    return program[::-1].replace('SC', 'CS', 1)[::-1]

def minimum_hacks(program, damage):
    """Finds minimum number of hacks needed if possible."""
    num_hacks = 0
    while 'CS' in program and calculate_damage(program) > max_damage:
        program = hack_once(program)
        num_hacks += 1

    if calculate_damage(program) <= max_damage:
        return num_hacks
    else:
        return 'IMPOSSIBLE'

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    max_damage, program = input().split()
    max_damage = int(max_damage)

    min_hacks = minimum_hacks(program, max_damage)
    print('Case #{}: {}'.format(case, min_hacks))
