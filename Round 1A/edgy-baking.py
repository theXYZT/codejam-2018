# Codejam 2018, Round 1A: Edgy Baking

from operator import attrgetter
from collections import namedtuple
from math import sqrt

# Object for an interval/range of perimeters
PerimeterRange = namedtuple("PerimeterRange", ["min", "max"])

class Cookie():
    """Class for a cookie."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.perimeter = 2*(self.width + self.height)
        self.cutrange = PerimeterRange(2*min(self.width, self.height), 
                                       2*sqrt(self.width**2 + self.height**2))


def merge_intervals(intervals):
    """Reduces a list of intervals by merging overlapping intervals."""
    intervals = sorted(intervals, key=attrgetter('min'))
    temp_interval = intervals.pop(0)
    merged_intervals = []
    for interval in intervals:
        if interval.min <= temp_interval.max:
            temp_interval = PerimeterRange(temp_interval.min,
            							   max(temp_interval.max, 
            							   	   interval.max))
        else:
            merged_intervals.append(temp_interval)
            temp_interval = interval
    merged_intervals.append(temp_interval)
    return merged_intervals

def process_case(max_perimeter, cookies):
    """Finds optimal perimeter given maximum and list of cookies."""
    current_perimeter = sum([cookie.perimeter for cookie in cookies])
    intervals = [PerimeterRange(current_perimeter, current_perimeter),]

    # Get intervals that can be reached by cutting cookies
    for cookie in cookies:
        intervals.extend([PerimeterRange(i.min + cookie.cutrange.min,
                                         i.max + cookie.cutrange.max)
                          for i in intervals])
        intervals = merge_intervals(intervals)

    # Only need the last interval that begins before the maximum perimeter
    best_interval = [i for i in intervals if i.min <= max_perimeter][-1]
    if best_interval.min <= max_perimeter <= best_interval.max:
        best_perimeter = max_perimeter
    else:
        best_perimeter = best_interval.max
    return best_perimeter

# I/O Code
num_cases = int(input())
for case_number in range(1, num_cases + 1):
    N, P = [int(i) for i in input().split(" ")]

    cookies = []
    for _ in range(N):
        W, H = [int(i) for i in input().split(" ")]
        cookies.append(Cookie(W, H))

    best_perimeter = process_case(P, cookies)
    print("Case #{}: {:.6f}".format(case_number, best_perimeter))
