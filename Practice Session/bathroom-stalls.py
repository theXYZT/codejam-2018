# Codejam 2018, Practice Session: Bathroom Stalls

def left_and_right(interval):
    """Splits an interval into left and right intervals."""
    return (interval - 1) // 2, interval // 2

def add_interval(intervals, interval, num_intervals):
    """Add required intervals to list of intervals."""
    if interval in intervals:
        intervals[interval] += num_intervals
    else:
        intervals[interval] = num_intervals

def add_people(intervals):
    """Split the largest intervals."""
    interval = max(intervals)
    num_intervals = intervals.pop(interval)
    
    left, right = left_and_right(interval)

    if left > 0:
        add_interval(intervals, left, num_intervals)
    if right > 0:
        add_interval(intervals, right, num_intervals)

def process_case(num_stalls, num_people):
    """Process test cases given number of stalls and people."""
    intervals = {num_stalls: 1}
    people_left = num_people
    while intervals[max(intervals)] < people_left:
        people_left -= intervals[max(intervals)]
        add_people(intervals)
    return left_and_right(max(intervals))

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_stalls, num_people = [int(i) for i in input().split()]

    min_LR, max_LR = process_case(num_stalls, num_people)
    print('Case #{}: {} {}'.format(case, max_LR, min_LR))
