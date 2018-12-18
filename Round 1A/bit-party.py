# Codejam 2018, Round 1A: Bit Party

from collections import namedtuple

# Object for input case parameters
Case = namedtuple('Case', ['robots', 'bits', 'cashiers'])

class Cashier():
    """Class for Cashier."""
    def __init__(self, max_items, scan_time, overhead):
        self.max_items = max_items
        self.scan_time = scan_time
        self.overhead = overhead
        self.max_time = self.max_items * self.scan_time + self.overhead

    def num_bits_in_time(self, t):
        """No. of bits cashier can process in time t."""
        max_time = self.max_time
        if t >= max_time:
            num_bits = self.max_items
        else:
            num_bits = (t - self.overhead) // self.scan_time
        return max(0, num_bits)


def test_time(t, case):
    """Finds if problem can be solved in time t."""
    num_bits_cashier = [x.num_bits_in_time(t) for x in case.cashiers]
    sorted_cashier_bits = sorted(num_bits_cashier, reverse=True)
    total_bits = sum(sorted_cashier_bits[:case.robots])
    return total_bits >= case.bits

def process_case(case):
    """Runs binary search for smallest time t that works."""
    min_time = 0
    max_time = max([cashier.max_time for cashier in case.cashiers])
    while max_time - min_time > 1:
        temp_time = (max_time + min_time) // 2
        if test_time(temp_time, case):
            max_time = temp_time
        else:
            min_time = temp_time
    return max_time

# I/O code
num_cases = int(input())

for case_number in range(1, num_cases + 1):
    R, B, C = [int(i) for i in input().split(" ")]

    cashiers = []
    for _ in range(C):
        M, S, P = [int(i) for i in input().split(" ")]
        cashiers.append(Cashier(M, S, P))

    case = Case(R, B, cashiers)
    best_time = process_case(case)
    print("Case #{}: {}".format(case_number, best_time))
