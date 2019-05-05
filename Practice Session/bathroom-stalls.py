# Codejam 2018, Practice Session: Bathroom Stalls

from collections import defaultdict

def get_left_right(interval):
    """Get left and right sub-intervals for an interval."""
    return (interval - 1) // 2, interval // 2

def split_longest_interval(intervals):
    """Split longest intervals."""
    longest = max(intervals)
    num_intervals = intervals.pop(longest)
    left, right = get_left_right(longest)

    if left:
        intervals[left] += num_intervals
    if right:
        intervals[right] += num_intervals

def solve_case(num_stalls, num_people):
    intervals = defaultdict(int)
    intervals[num_stalls] = 1

    while intervals[max(intervals)] < num_people:
        num_people -= intervals[max(intervals)]
        split_longest_interval(intervals)

    return get_left_right(max(intervals))

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_stalls, num_people = map(int, input().split())

    min_LR, max_LR = solve_case(num_stalls, num_people)
    print('Case #{}: {} {}'.format(case, max_LR, min_LR))
