# Codejam 2018, Round 2: Graceful Chainsaw Jugglers

import math
from functools import lru_cache

@lru_cache(maxsize=None)
def max_blue(red, jugglers):
    """Finds maximum possible value of blue."""
    if jugglers == 0:
        return 0

    if red == 0:
        return jugglers * (jugglers - 1) // 2

    blue = math.inf
    
    N = 1
    while N * (N - 1) <= 2 * red and N <= jugglers:
        temp = max_blue(red - N * (N - 1) // 2, jugglers - N) + jugglers - N
        blue = temp if temp < blue else blue
        N += 1
    return blue

def get_jugglers(red, blue):
    """Returns max number of jugglers that satisfy conditions."""
    jugglers = 0
    while max_blue(red, jugglers) <= blue:
        jugglers += 1
    return jugglers - 2

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    red, blue = [int(i) for i in input().split()]
    jugglers = get_jugglers(red, blue)
    print('Case #{}: {}'.format(case, jugglers))
